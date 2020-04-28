import pygame
from enum import Enum

white_king = pygame.image.load('client/images/white_king.png')
white_queen = pygame.image.load('client/images/white_queen.png')
white_bishop = pygame.image.load('client/images/white_bishop.png')
white_knight = pygame.image.load('client/images/white_knight.png')
white_rook = pygame.image.load('client/images/white_rook.png')
white_pawn = pygame.image.load('client/images/white_pawn.png')

black_king = pygame.image.load('client/images/black_king.png')
black_queen = pygame.image.load('client/images/black_queen.png')
black_bishop = pygame.image.load('client/images/black_bishop.png')
black_knight = pygame.image.load('client/images/black_knight.png')
black_rook = pygame.image.load('client/images/black_rook.png')
black_pawn = pygame.image.load('client/images/black_pawn.png')


class Color(Enum):
    WHITE = 1
    BLACK = 2


class Piece:

    def __init__(self, color):
        self.color = color
        self.image = None
        self.piece_rect = None

    def get_color(self):
        """
        Get the piece color.
        ::return Color: piece color
        """
        return self.color

    def get_rect(self):
        """
        Get the piece rect.
        ::return pygame.Rect: the piece rect
        """
        return self.piece_rect

    def set_rect(self, piece_rect):
        """
        Set the piece rect.
        ::param piece_rect: the piece rect
        """
        self.piece_rect = piece_rect

    def draw(self, surface):
        """
        Draw the piece to the screen's surface.
        ::param surface: display surface to draw on
        """
        # Scale the piece's image
        image_scaled = pygame.transform.scale(
            self.image, (self.piece_rect.width, self.piece_rect.height))

        # Draw the piece's image
        surface.blit(image_scaled, self.piece_rect)


class King(Piece):

    def __init__(self, color):
        super().__init__(color)

        self.color = color

        if self.color == Color.WHITE:
            self.image = white_king
        else:
            self.image = black_king


class Queen(Piece):

    def __init__(self, color):
        super().__init__(color)

        self.color = color

        if self.color == Color.WHITE:
            self.image = white_queen
        else:
            self.image = black_queen


class Bishop(Piece):

    def __init__(self, color):
        super().__init__(color)

        self.color = color

        if self.color == Color.WHITE:
            self.image = white_bishop
        else:
            self.image = black_bishop


class Knight(Piece):

    def __init__(self, color):
        super().__init__(color)

        self.color = color

        if self.color == Color.WHITE:
            self.image = white_knight
        else:
            self.image = black_knight


class Rook(Piece):

    def __init__(self, color):
        super().__init__(color)

        self.color = color

        if self.color == Color.WHITE:
            self.image = white_rook
        else:
            self.image = black_rook


class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color)

        self.color = color

        if self.color == Color.WHITE:
            self.image = white_pawn
        else:
            self.image = black_pawn
