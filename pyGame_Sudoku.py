import pygame

width, height = 750, 750
bg_color = (255, 255, 255)


def main():
    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sudoku app")
    window.fill(bg_color)

    for i in range(10):
        pygame.draw.line(window, (0,0,0), (), (), 2)
        pygame.draw.line(window, (0, 0, 0), (), (), 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


if __name__ == '__main__':
    main()
