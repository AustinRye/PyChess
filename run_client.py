import pygame


if __name__ == '__main__':
    pygame.init()

    from client import game
    game.run()

    pygame.quit()
