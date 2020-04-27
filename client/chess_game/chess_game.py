import pygame

from client.chess_game.board import Board


class ChessGame:

    def __init__(self):
        self.board = Board()

    def reset(self):
        pass

    def draw(self, surface):
        """
        Draw the chess game to the screen's surface.
        ::param surface: display surface to draw on
        """
        surface_rect = surface.get_rect()

        # Draw the board
        board_width = 560
        board_height = 560
        board_left = (surface_rect.width-board_width)/2
        board_top = (surface_rect.height-board_height)/2
        board_rect = pygame.Rect(
            (board_left, board_top), (board_width, board_height))
        self.board.draw(surface, board_rect)
