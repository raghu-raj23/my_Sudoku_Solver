import pygame
import requests

WIDTH, HEIGHT = 550, 550
bg_color = (255, 255, 255)
font_color = (25, 255, 25)
buffer = 5
font_face = ('Helvetica', 35)
difficulty = {0: "easy", 1: "medium", 2: "hard", 3: "random"}
chosen_diff = 3

# Get the sudoku board using API
response = requests.get(f'https://sugoku.herokuapp.com/board?difficulty={difficulty[chosen_diff]}')
grid = response.json()['board']
grid_ori = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]
grid_a = response.json()['board']


# Function to check if the cell is empty
def is_empty(num):
    if num == 0:
        return True
    return False


# Check if the number at the particular position/cell is valid or not
def is_valid(num, pos):
    for i in range(len(grid_a[0])):
        if grid_a[pos[0]][i] == num:
            return False

    for i in range(len(grid_a[0])):
        if grid_a[i][pos[1]] == num:
            return False

    # This is to check inside the sub squares
    box_y = pos[1] // 3 * 3
    box_x = pos[0] // 3 * 3

    for i in range(3):
        for j in range(3):
            if grid_a[box_x + i][box_y + j] == num:
                return False
    return True


# A flag for exit condition
flag = 0


def solver(win):
    my_font = pygame.font.SysFont(*font_face)
    for i in range(len(grid_a[0])):
        for j in range(len(grid_a[0])):
            if is_empty(grid_a[i][j]):
                # Backtracking algorithm in action
                for k in range(1, 10):
                    if is_valid(k, (i, j)):
                        grid_a[i][j] = k
                        pygame.draw.rect(win, bg_color,
                                         ((j + 1) * 50 + buffer - 2, (i + 1) * 50 + buffer - 2, 50 - 2 * buffer,
                                          50 - 2 * buffer))
                        value = my_font.render(str(k), True, (0, 0, 255))
                        win.blit(value, ((j + 1) * 50 + 16, (i + 1) * 50 + 7))
                        pygame.display.update()
                        pygame.time.delay(5)

                        solver(win)
                        # checking for the exit condition
                        global flag
                        if flag == 1:
                            value = my_font.render("Solved", True, (255, 25, 25))
                            win.blit(value, (220, 500))
                            pygame.display.update()
                            return
                        # If solution not found, the cell/position is reset
                        grid_a[i][j] = 0
                        pygame.draw.rect(win, bg_color,
                                         ((j + 1) * 50 + buffer - 2, (i + 1) * 50 + buffer - 2, 50 - 2 * buffer,
                                          50 - 2 * buffer))
                        pygame.display.update()
                return
    flag = 1


# A function to manually insert values into the grid
def insert(win, position):
    i, j = position[1] - 1, position[0] - 1
    my_font = pygame.font.SysFont(*font_face)
    pygame.draw.rect(win, (255, 0, 0),
                     (position[0] * 50 + buffer - 2, position[1] * 50 + buffer - 2, 50 - buffer + 2,
                      50 - buffer + 2))
    pygame.draw.rect(win, bg_color,
                     (position[0] * 50 + buffer, position[1] * 50 + buffer, 50 - 2 * buffer + 2,
                      50 - 2 * buffer + 2))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if grid_ori[i][j] != 0:
                    return
                if event.key == 48:
                    grid[i][j] = event.key - 48
                    pygame.draw.rect(win, bg_color,
                                     (position[0] * 50 + buffer - 2, position[1] * 50 + buffer - 2, 50 - buffer + 2,
                                      50 - buffer + 2))
                    pygame.display.update()
                    return
                if 0 < event.key - 48 < 10:
                    pygame.draw.rect(win, bg_color,
                                     (position[0] * 50 + buffer - 2, position[1] * 50 + buffer - 2, 50 - buffer + 2,
                                      50 - buffer + 2))
                    value = my_font.render(str(event.key - 48), True, (0, 0, 0))
                    win.blit(value, (position[0] * 50 + 16, position[1] * 50 + 7))
                    grid[i][j] = event.key - 48
                    pygame.display.update()
                    return
                return


# A function to build the initial setup of the board
def build(win, board, color=font_color):
    win.fill(bg_color)
    my_font = pygame.font.SysFont(*font_face)
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)
        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    pygame.display.update()

    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if 0 < board[i][j] < 10:
                value = my_font.render(str(board[i][j]), True, color)
                win.blit(value, ((j + 1) * 50 + 16, (i + 1) * 50 + 7))
    pygame.display.update()


# The main function
def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku Solver")
    win.fill(bg_color)
    build(win, grid)

    while True:
        for event in pygame.event.get():
            # Checks if the key pressed is 's'
            if event.type == pygame.KEYDOWN and event.key == 115:
                global grid_a
                build(win, grid_a)
                solver(win)
            #     Checks for left mouse click
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = list(pygame.mouse.get_pos())
                if 0 < pos[0] // 50 < 10 and 0 < pos[1] // 50 < 10:
                    insert(win, [pos[0] // 50, pos[1] // 50])
            if event.type == pygame.QUIT:
                pygame.quit()
                return


if __name__ == '__main__':
    main()
