import pygame


if __name__ == '__main__':
    pygame.init()

    from client import game_manager
    game_manager.run()

    pygame.quit()
