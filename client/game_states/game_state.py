import pygame


class GameState:

    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state_name = None
        self.persistent = None
        self.surface_rect = pygame.display.get_surface().get_rect()

        self.setupGraphics()

    def setupGraphics(self):
        """
        Setup the graphics before drawing to the screen.
        """
        pass

    def startup(self, persistent):
        """
        Called when a state resumes being active.
        Allows information to be passed between states.
        ::param persistent: dict passed from previous state
        """
        self.persistent = persistent

    def process_event(self, event):
        """
        Process a single pygame event.
        """
        pass

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
        pass
