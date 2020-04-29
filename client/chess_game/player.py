import pygame
from enum import Enum


class Player:

    def __init__(self, color):
        self.color = color
        self.previous_square = None
        self.selected_piece = None

    def get_color(self):
        """
        Get the player color.
        ::return Color: player color
        """
        return self.color

    def get_previous_square(self):
        """
        Get the previous square.
        ::return Square: previous square
        """
        return self.previous_square

    def get_selected_piece(self):
        """
        Get the selected piece.
        ::return Piece: selected piece
        """
        return self.selected_piece

    def pick_piece(self, square):
        """
        Select piece.
        ::param piece: selected square
        """
        self.previous_square = square
        self.selected_piece = square.remove_piece()

    def is_legal_move(self):
        if (2, 2) in self.legal_moves:
            print('yes')

    def place_piece(self, square):
        """
        Place the piece on the square.
        """
        self.previous_square = None
        square.add_piece(self.selected_piece)
        self.selected_piece = None

    def replace_piece(self, square):
        """
        Replace the piece on the square.
        ::return Square: square to replace the piece
        """
        self.previous_square = None
        previous_piece = square.replace_piece(self.selected_piece)
        self.selected_piece = None
        return previous_piece

    def cancel_selected_piece(self):
        """
        Place the piece back to its previous square.
        """
        self.previous_square.add_piece(self.selected_piece)
        self.previous_square = None
        self.selected_piece = None

    def draw_selected_piece(self, surface):
        """
        Draw the selected piece at the player's mouse position.
        ::param surface: display surface to draw on
        """
        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Get the previous square width and height
        square_width = self.previous_square.get_rect().width
        square_height = self.previous_square.get_rect().height

        # Expand piece rect
        piece_width_expanded = square_width + 10
        piece_height_expanded = square_height + 10
        piece_left_expanded = mouse_pos[0] - piece_width_expanded//2
        piece_top_expanded = mouse_pos[1] - piece_height_expanded//2
        piece_rect_expanded = pygame.Rect(
            (piece_left_expanded, piece_top_expanded), (piece_width_expanded, piece_height_expanded))

        # Set the piece's rect
        self.selected_piece.set_rect(piece_rect_expanded)

        # Draw the piece
        self.selected_piece.draw(surface)
