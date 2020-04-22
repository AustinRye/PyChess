import pygame
import pygame_gui

from client.game_states.game_state import GameState


class OfflineMultiplayerState(GameState):

    def setupGraphics(self):
        """
        Setup the graphics before drawing to the screen.
        """
        # Initialize font
        self.font = pygame.font.Font(None, 24)

        # Initialize colors
        self.white = (255, 255, 255)

        # Initialize GUI manager
        self.gui_manager = pygame_gui.UIManager(self.surface_rect.size)

        # Initialize offline multiplayer label
        width = 120
        height = 50
        left = self.surface_rect.height/2 - width/2
        top = self.surface_rect.width/2 - height/2 - 200
        self.offline_multiplayer_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((left, top), (width, height)),
                                                                     text='Offline Multiplayer',
                                                                     manager=self.gui_manager)

    def process_event(self, event):
        """
        Called when a state resumes being active.
        Allows information to be passed between states.
        ::param persistent: dict passed from previous state
        """
        if event.type == pygame.QUIT:
            self.quit = True

        self.gui_manager.process_events(event)

    def update(self, dt):
        """
        Update the game state.
        """
        self.gui_manager.update(dt)

    def draw(self, surface):
        """
        Draw everything to the screen's surface.
        """
        surface.fill(self.white)

        self.gui_manager.draw_ui(surface)
