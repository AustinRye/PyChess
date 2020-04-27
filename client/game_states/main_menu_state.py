import pygame
import pygame_gui

from client.game_states.game_state import GameState


class MainMenuState(GameState):

    def setupGraphics(self, surface):
        """
        Setup the graphics before drawing to the screen.
        ::param surface: display surface to draw on
        """
        # Initialize font
        self.font = pygame.font.Font(None, 24)

        # Initialize colors
        self.white = (255, 255, 255)

        # Initialize GUI manager
        self.gui_manager = pygame_gui.UIManager(self.surface_rect.size)

        # Initialize pychess label
        width = 120
        height = 50
        left = self.surface_rect.height/2 - width/2
        top = self.surface_rect.width/2 - height/2 - 200
        self.pychess_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((left, top), (width, height)),
                                                         text='PyChess',
                                                         manager=self.gui_manager)

        # Initialize singleplayer button
        width = 120
        height = 50
        left = self.surface_rect.height/2 - width/2
        top = self.surface_rect.width/2 - height/2 + 80
        self.singleplayer_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((left, top), (width, height)),
                                                                text='Singleplayer',
                                                                manager=self.gui_manager)

        # Initialize offline multiplayer button
        width = 180
        height = 50
        left = self.surface_rect.height/2 - width/2
        top = self.surface_rect.width/2 - height/2 + 160
        self.offline_multiplayer_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((left, top), (width, height)),
                                                                       text='Offline Multiplayer',
                                                                       manager=self.gui_manager)

        # Initialize online multiplayer button
        width = 180
        height = 50
        left = self.surface_rect.height/2 - width/2
        top = self.surface_rect.width/2 - height/2 + 240
        self.online_multiplayer_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((left, top), (width, height)),
                                                                      text='Online Multiplayer',
                                                                      manager=self.gui_manager)

    def process_event(self, event):
        """
        Called when a state resumes being active.
        Allows information to be passed between states.
        ::param persistent: dict passed from previous state
        """
        if event.type == pygame.QUIT:
            self.quit = True

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.singleplayer_button:
                    self.next_state_name = 'SingleplayerState'
                    self.done = True
                if event.ui_element == self.offline_multiplayer_button:
                    self.next_state_name = 'OfflineMultiplayerState'
                    self.done = True
                if event.ui_element == self.online_multiplayer_button:
                    self.next_state_name = 'OnlineMultiplayerState'
                    self.done = True

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
