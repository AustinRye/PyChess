import pygame
import pygame_gui

from client.game_states.game_state import GameState
from client.chess_game.chess_game import ChessGame
from client.chess_game.pieces import Color


class OfflineMultiplayerState(GameState):

    def __init__(self):
        super().__init__()

        self.chess_game = ChessGame()

    def setupGraphics(self, surface):
        """
        Setup the graphics before drawing to the screen.
        ::param surface: display surface to draw on
        """
        # Initialize GUI manager
        self.gui_manager = pygame_gui.UIManager(self.surface_rect.size)

        # Initialize colors
        self.white = (255, 255, 255)

        # Initialize board size
        board_width = 560
        board_height = 560
        board_left = (self.surface_rect.width-board_width)/2
        board_top = (self.surface_rect.height-board_height)/2
        board_rect = pygame.Rect(
            (board_left, board_top), (board_width, board_height))
        self.chess_game.board.set_rect(board_rect)

        # Initialize win label
        width = 200
        height = 50
        left = self.surface_rect.width/2 - width/2
        top = 10
        self.game_state_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((left, top), (width, height)),
                                                            text='Game State',
                                                            manager=self.gui_manager)

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

        self.gui_manager.process_events(event)

    def update(self, dt):
        """
        Update the game state.
        ::param dt: milliseconds since last tick
        """
        if self.chess_game.win:
            player_color = 'White' if self.chess_game.win.get_color() == Color.WHITE else 'Black'
            self.game_state_label.set_text(f'{player_color} Wins!')
        else:
            player_turn = 'White' if self.chess_game.player_turn.get_color() == Color.WHITE else 'Black'
            self.game_state_label.set_text(f"{player_turn}'s Turn")
        self.gui_manager.update(dt)

    def draw(self, surface):
        """
        Draw everything to the screen's surface.
        ::param surface: display surface to draw on
        """
        surface.fill(self.white)

        self.chess_game.draw(surface)

        self.gui_manager.draw_ui(surface)
