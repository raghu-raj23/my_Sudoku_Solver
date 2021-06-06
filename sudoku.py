# game_board = [
#     [0, 0, 0, 0, 0, 0, 6, 8, 0],
#     [0, 0, 0, 0, 7, 3, 0, 0, 9],
#     [3, 0, 9, 0, 0, 0, 0, 4, 5],
#     [4, 9, 0, 0, 0, 0, 0, 0, 0],
#     [8, 0, 3, 0, 5, 0, 9, 0, 2],
#     [0, 0, 0, 0, 0, 0, 0, 3, 6],
#     [9, 6, 0, 0, 0, 0, 3, 0, 8],
#     [7, 0, 0, 6, 8, 0, 0, 0, 0],
#     [0, 2, 8, 0, 0, 0, 0, 0, 0]
# ]
game_board = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]


def solve(board):
    # print_board(board)
    # print("========================")
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0
    return False


def is_valid(board, num, pos):
    # Check for the cols to be valid
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check for the rows to be valid
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check for the inner box to be valid
    # Board divided as smaller boxes of size 3x3
    box_x = pos[1] // 3  # cols
    box_y = pos[0] // 3  # rows

    # This will loop inside the 3x3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j  # row, col
    return None


print_board(game_board)
print("--------------------------------------------")
solve(game_board)
print_board(game_board)
