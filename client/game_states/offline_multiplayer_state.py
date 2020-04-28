import pygame
import pygame_gui

from client.game_states.game_state import GameState
from client.chess_game.chess_game import ChessGame


class OfflineMultiplayerState(GameState):

    def __init__(self):
        super().__init__()

        self.chess_game = ChessGame()

    def setupGraphics(self, surface):
        """
        Setup the graphics before drawing to the screen.
        ::param surface: display surface to draw on
        """
        surface_rect = surface.get_rect()

        # Initialize colors
        self.white = (255, 255, 255)

        # Initialize board size
        board_width = 560
        board_height = 560
        board_left = (surface_rect.width-board_width)/2
        board_top = (surface_rect.height-board_height)/2
        board_rect = pygame.Rect(
            (board_left, board_top), (board_width, board_height))
        self.chess_game.board.set_rect(board_rect)

    def startup(self, persistent):
        super().startup(persistent)

        self.chess_game.reset()

    def process_event(self, event):
        """
        Called when a state resumes being active.
        Allows information to be passed between states.
        ::param persistent: dict passed from previous state
        """
        LEFT_CLICK = 1

        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == LEFT_CLICK:
                mouse_pos = pygame.mouse.get_pos()
                self.chess_game.handle_mouse_down(mouse_pos[0], mouse_pos[1])
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == LEFT_CLICK:
                mouse_pos = pygame.mouse.get_pos()
                self.chess_game.handle_mouse_up(mouse_pos[0], mouse_pos[1])

    def update(self, dt):
        """
        Update the game state.
        ::param dt: milliseconds since last tick
        """
        pass

    def draw(self, surface):
        """
        Draw everything to the screen's surface.
        ::param surface: display surface to draw on
        """
        surface.fill(self.white)

        self.chess_game.draw(surface)
