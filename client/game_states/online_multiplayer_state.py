import pygame
import pygame_gui

from client.game_states.game_state import GameState


class OnlineMultiplayerState(GameState):

    def setupGraphics(self, surface):
        """
        Setup the graphics before drawing to the screen.
        ::param surface: display surface to draw on
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
        """
        pass

    def draw(self, surface):
        """
        Draw everything to the screen's surface.
        """
        surface.fill(self.white)
