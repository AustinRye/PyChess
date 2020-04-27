import pygame
import pygame_gui

from client.game_states.game_state import GameState
from client.chess_game.chess_game import ChessGame


class OfflineMultiplayerState(GameState):

    def __init__(self):
        super().__init__()

        self.chess_game = ChessGame()

    def setupGraphics(self):
        """
        Setup the graphics before drawing to the screen.
        """
        # Initialize colors
        self.white = (255, 255, 255)

    def process_event(self, event):
        """
        Called when a state resumes being active.
        Allows information to be passed between states.
        ::param persistent: dict passed from previous state
        """
        if event.type == pygame.QUIT:
            self.quit = True

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
