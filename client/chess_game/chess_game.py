import pygame

from client.chess_game.board import Board
from client.chess_game.player import Player


class ChessGame:

    def __init__(self):
        self.board = Board()

        self.player = Player(None)

    def reset(self):
        """
        Reset the chess game.
        """
        self.board.reset()

    def handle_mouse_down(self, x, y):
        """
        Handle mouse down event.
        ::param x: x position
        ::param y: y position
        """
        if self.board.is_within_bounds(x, y):  # Coordinates within board bounds
            square = self.board.get_square(x, y)
            if not self.player.get_selected_piece():  # Player has no selected piece
                if square.is_occupied():  # Square is occupied
                    # Pick up the piece at the selected square
                    self.player.pick_piece(square)

    def handle_mouse_up(self, x, y):
        """
        Handle mouse up event.
        ::param x: x position
        ::param y: y position
        """
        if self.board.is_within_bounds(x, y):  # Coordinates within board bounds
            square = self.board.get_square(x, y)
            if self.player.get_selected_piece():  # Player has a selected piece
                if square.is_occupied():  # Square is occupied
                    # Replace the piece at the selected square
                    self.player.replace_piece(square)
                else:
                    # Place the piece at the selected square
                    self.player.place_piece(square)

    def draw(self, surface):
        """
        Draw the chess game to the screen's surface.
        ::param surface: display surface to draw on
        """
        surface_rect = surface.get_rect()

        # Draw the board
        self.board.draw(surface)

        # Draw the player's selected piece
        self.player.drawSelectedPiece(
            surface, self.board.piece_width, self.board.piece_height)
