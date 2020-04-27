import pygame

from client.chess_game.board import Board


class ChessGame:

    def __init__(self):
        self.board = Board()

    def reset(self):
        """
        Reset the chess game.
        """
        self.board.reset()

    def handle_mouse_down(self, mouse_pos):
        """
        Handle mouse down event.
        ::param mouse_pos: mouse position
        """
        print(self.board.is_within_bounds(mouse_pos[0], mouse_pos[1]))

    def draw(self, surface):
        """
        Draw the chess game to the screen's surface.
        ::param surface: display surface to draw on
        """
        surface_rect = surface.get_rect()

        # Draw the board
        self.board.draw(surface)
