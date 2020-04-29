import pygame


class Square:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.piece = None
        self.square_rect = None

    def get_row(self):
        """
        Get the square's row.
        ::return int: row
        """
        return self.row

    def get_col(self):
        """
        Get the square's col.
        ::return int: col
        """
        return self.col

    def get_piece(self):
        """
        Get the piece.
        ::return Piece: piece on the square
        """
        return self.piece

    def add_piece(self, piece):
        """
        Add the piece to the square.
        ::param piece: add the piece to the square
        """
        self.piece = piece
        self.set_piece_rect(self.square_rect)

    def remove_piece(self):
        """
        Remove the piece from the square.
        ::return Piece: piece removed from the square
        """
        piece = self.piece
        self.piece = None
        return piece

    def replace_piece(self, newPiece):
        """
        Replace the piece on the square.
        ::param newPiece: piece to add to the square
        ::return Piece: piece removed from the square
        """
        oldPiece = self.remove_piece()
        self.add_piece(newPiece)
        return oldPiece

    def is_occupied(self):
        """
        Check if square is occupied.
        ::return bool: True if square is occupied by a piece, False if not
        """
        return (not self.piece == None)

    def get_rect(self):
        """
        Get the square rect.
        ::return pygame.Rect: the square rect
        """
        return self.square_rect

    def set_rect(self, square_rect):
        """
        Set the square rect.
        ::param square_rect: the square rect
        """
        self.square_rect = square_rect

        self.set_piece_rect(self.square_rect)

    def set_piece_rect(self, square_rect):
        """
        Set piece rect relative to square rect.
        ::param square_rect: the square rect
        """
        piece_width = square_rect.width - 10
        piece_height = square_rect.height - 10

        if self.is_occupied():
            piece_rect = pygame.Rect((square_rect.left+(square_rect.width-piece_width)//2,
                                      square_rect.top+(square_rect.height-piece_height)//2), (piece_width, piece_height))
            self.piece.set_rect(piece_rect)

    def is_within_bounds(self, x, y):
        """
        Check if position is within the square bounds.
        ::param x: x position
        ::param y: y position
        ::return bool: True if position within square bounds, else False
        """
        return (self.square_rect.left < x < self.square_rect.right and self.square_rect.top < y < self.square_rect.bottom)

    def draw(self, surface, square_color):
        """
        Draw the square to the screen's surface.
        ::param surface: display surface to draw on
        """
        # Draw the square
        pygame.draw.rect(surface, square_color, self.square_rect)

        # Draw the piece if occupied
        if self.is_occupied():
            self.piece.draw(surface)
