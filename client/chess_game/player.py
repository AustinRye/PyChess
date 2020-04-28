import pygame
from enum import Enum


class Player:

    def __init__(self, color):
        self.color = color
        self.previous_square = None
        self.selected_piece = None

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
        self.previous_square.addPiece(self.selected_piece)
        self.previous_square = None
        self.selected_piece = None

    def drawSelectedPiece(self, surface, board_piece_width, board_piece_height):
        """
        Draw the selected piece at the player's mouse position.
        ::param surface: display surface to draw on
        ::param board_piece_width: the board's piece width
        ::param board_piece_height: the board's piece height
        """
        if self.selected_piece:
            selected_piece_width = board_piece_width + 20
            selected_piece_height = board_piece_height + 20

            mouse_pos = pygame.mouse.get_pos()

            image = pygame.transform.scale(
                self.selected_piece.get_image(), (selected_piece_width, selected_piece_height))
            image_rect = ((mouse_pos[0]-selected_piece_width/2, mouse_pos[1] -
                           selected_piece_height/2), (selected_piece_width, selected_piece_height))
            surface.blit(image, image_rect)
