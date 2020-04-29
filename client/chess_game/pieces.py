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

    def get_valid_moves(self, rowCount, colCount, squares, src):
        """
        Get a list of valid moves.
        ::return list: list with row and col tuples
        """
        pass

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

    def is_danger_move(self, row_count, col_count, squares, src_square):
        """
        Check if square is a danger move.
        ::param row_count: the row count
        ::param col_count: the col count
        ::param squares: the board squares
        """
        # Mark as danger move if the square corresponds to a piece's valid move
        for row in range(row_count):
            for col in range(col_count):
                square = squares[row][col]
                if square.is_occupied():
                    piece = square.get_piece()
                    if not piece.get_color() == self.color:
                        valid_moves = piece.get_valid_moves(
                            row_count, col_count, squares, square)
                        if src_square in valid_moves:
                            return True

        return False

    def get_valid_moves(self, row_count, col_count, squares, src_square):
        """
        Get a list of valid moves.
        ::return list: list of squares
        """
        valid_moves = []

        src_row = src_square.get_row()
        src_col = src_square.get_col()

        # Move down
        if (0 <= src_row+1 <= row_count-1):
            dest_square = squares[src_row+1][src_col]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)

        # Move up
        if (0 <= src_row-1 <= row_count-1):
            dest_square = squares[src_row-1][src_col]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)

        # Move right
        if (0 <= src_col+1 <= col_count-1):
            dest_square = squares[src_row][src_col+1]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)

        # Move left
        if (0 <= src_col-1 <= col_count-1):
            dest_square = squares[src_row][src_col-1]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)

        # Move down right
        if (0 <= src_row+1 <= row_count-1 and 0 <= src_col+1 <= col_count-1):
            dest_square = squares[src_row+1][src_col+1]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)

        # Move down left
        if (0 <= src_row+1 <= row_count-1 and 0 <= src_col-1 <= col_count-1):
            dest_square = squares[src_row+1][src_col-1]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)

        # Move up right
        if (0 <= src_row-1 <= row_count-1 and 0 <= src_col+1 <= col_count-1):
            dest_square = squares[src_row-1][src_col+1]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)

        # Move up left
        if (0 <= src_row-1 <= row_count-1 and 0 <= src_col-1 <= col_count-1):
            dest_square = squares[src_row-1][src_col-1]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)

        return valid_moves


class Queen(Piece):

    def __init__(self, color):
        super().__init__(color)

        self.color = color

        if self.color == Color.WHITE:
            self.image = white_queen
        else:
            self.image = black_queen

    def get_valid_moves(self, row_count, col_count, squares, src_square):
        """
        Get a list of valid moves.
        ::return list: list of squares
        """
        valid_moves = []

        src_row = src_square.get_row()
        src_col = src_square.get_col()

        # Move horizontally right
        for dx in range(1, col_count-src_col):
            dest_square = squares[src_row][src_col+dx]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
                break

        # Move horizontally left
        for dx in range(1, src_col+1):
            dest_square = squares[src_row][src_col-dx]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
                break

        # Move vertically down
        for dy in range(1, row_count-src_row):
            dest_square = squares[src_row+dy][src_col]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
                break

        # Move vertically up
        for dy in range(1, src_row+1):
            dest_square = squares[src_row-dy][src_col]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
                break

        # Move diagonally down right
        dx = col_count-1 - src_col
        dy = row_count-1 - src_row
        dmin = dx if dx <= dy else dy
        for step in range(0, dmin):
            dest_square = squares[src_row+step+1][src_col+step+1]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
                break

        # Move diagonally down left
        dx = src_col
        dy = row_count-1 - src_row
        dmin = dx if dx <= dy else dy
        for step in range(0, dmin):
            dest_square = squares[src_row+step+1][src_col-step-1]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
                break

        # Move diagonally up right
        dx = col_count-1 - src_col
        dy = src_row
        dmin = dx if dx <= dy else dy
        for step in range(0, dmin):
            dest_square = squares[src_row-step-1][src_col+step+1]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
                break

        # Move diagonally up left
        dx = src_col
        dy = src_row
        dmin = dx if dx <= dy else dy
        for step in range(0, dmin):
            dest_square = squares[src_row-step-1][src_col-step-1]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
                break

        return valid_moves


class Bishop(Piece):

    def __init__(self, color):
        super().__init__(color)

        self.color = color

        if self.color == Color.WHITE:
            self.image = white_bishop
        else:
            self.image = black_bishop

    def get_valid_moves(self, row_count, col_count, squares, src_square):
        """
        Get a list of valid moves.
        ::return list: list of squares
        """
        valid_moves = []

        src_row = src_square.get_row()
        src_col = src_square.get_col()

        # Move diagonally down right
        dx = col_count-1 - src_col
        dy = row_count-1 - src_row
        dmin = dx if dx <= dy else dy
        for step in range(0, dmin):
            dest_square = squares[src_row+step+1][src_col+step+1]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
                break

        # Move diagonally down left
        dx = src_col
        dy = row_count-1 - src_row
        dmin = dx if dx <= dy else dy
        for step in range(0, dmin):
            dest_square = squares[src_row+step+1][src_col-step-1]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
                break

        # Move diagonally up right
        dx = col_count-1 - src_col
        dy = src_row
        dmin = dx if dx <= dy else dy
        for step in range(0, dmin):
            dest_square = squares[src_row-step-1][src_col+step+1]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
                break

        # Move diagonally up left
        dx = src_col
        dy = src_row
        dmin = dx if dx <= dy else dy
        for step in range(0, dmin):
            dest_square = squares[src_row-step-1][src_col-step-1]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
                break

        return valid_moves


class Knight(Piece):

    def __init__(self, color):
        super().__init__(color)

        self.color = color

        if self.color == Color.WHITE:
            self.image = white_knight
        else:
            self.image = black_knight

    def get_valid_moves(self, row_count, col_count, squares, src_square):
        """
        Get a list of valid moves.
        ::return list: list of squares
        """
        valid_moves = []

        src_row = src_square.get_row()
        src_col = src_square.get_col()

        # Move down 2 and right 1
        if (0 <= src_row+2 <= row_count-1 and 0 <= src_col+1 <= col_count-1):
            dest_square = squares[src_row+2][src_col+1]
            # Occupied
            if dest_square.is_occupied():
                # Not the same color
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
            else:
                valid_moves.append(dest_square)

        # Move down 2 and left 1
        if (0 <= src_row+2 <= row_count-1 and 0 <= src_col-1 <= col_count-1):
            dest_square = squares[src_row+2][src_col-1]
            # Occupied
            if dest_square.is_occupied():
                # Not the same color
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
            else:
                valid_moves.append(dest_square)

        # Move up 2 and right 1
        if (0 <= src_row-2 <= row_count-1 and 0 <= src_col+1 <= col_count-1):
            dest_square = squares[src_row-2][src_col+1]
            # Occupied
            if dest_square.is_occupied():
                # Not the same color
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
            else:
                valid_moves.append(dest_square)

        # Move dup 2 and left 1
        if (0 <= src_row-2 <= row_count-1 and 0 <= src_col-1 <= col_count-1):
            dest_square = squares[src_row-2][src_col-1]
            # Occupied
            if dest_square.is_occupied():
                # Not the same color
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
            else:
                valid_moves.append(dest_square)

        # Move down 1 and right 2
        if (0 <= src_row+1 <= row_count-1 and 0 <= src_col+2 <= col_count-1):
            dest_square = squares[src_row+1][src_col+2]
            # Occupied
            if dest_square.is_occupied():
                # Not the same color
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
            else:
                valid_moves.append(dest_square)

        # Move up 1 and right 2
        if (0 <= src_row-1 <= row_count-1 and 0 <= src_col+2 <= col_count-1):
            dest_square = squares[src_row-1][src_col+2]
            # Occupied
            if dest_square.is_occupied():
                # Not the same color
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
            else:
                valid_moves.append(dest_square)

        # Move down 1 and left 2
        if (0 <= src_row+1 <= row_count-1 and 0 <= src_col-2 <= col_count-1):
            dest_square = squares[src_row+1][src_col-2]
            # Occupied
            if dest_square.is_occupied():
                # Not the same color
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
            else:
                valid_moves.append(dest_square)

        # Move up 1 and left 2
        if (0 <= src_row-1 <= row_count-1 and 0 <= src_col-2 <= col_count-1):
            dest_square = squares[src_row-1][src_col-2]
            # Occupied
            if dest_square.is_occupied():
                # Not the same color
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
            else:
                valid_moves.append(dest_square)

        return valid_moves


class Rook(Piece):

    def __init__(self, color):
        super().__init__(color)

        self.color = color

        if self.color == Color.WHITE:
            self.image = white_rook
        else:
            self.image = black_rook

    def get_valid_moves(self, row_count, col_count, squares, src_square):
        """
        Get a list of valid moves.
        ::return list: list of squares
        """
        valid_moves = []

        src_row = src_square.get_row()
        src_col = src_square.get_col()

        # Move horizontally right
        for dx in range(1, col_count-src_col):
            dest_square = squares[src_row][src_col+dx]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
                break

        # Move horizontally left
        for dx in range(1, src_col+1):
            dest_square = squares[src_row][src_col-dx]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
                break

        # Move vertically down
        for dy in range(1, row_count-src_row):
            dest_square = squares[src_row+dy][src_col]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
                break

        # Move vertically up
        for dy in range(1, src_row+1):
            dest_square = squares[src_row-dy][src_col]
            if not dest_square.is_occupied():
                valid_moves.append(dest_square)
            else:
                if not self.color == dest_square.get_piece().get_color():
                    valid_moves.append(dest_square)
                break

        return valid_moves


class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color)

        self.color = color

        if self.color == Color.WHITE:
            self.image = white_pawn
        else:
            self.image = black_pawn

        self.first_move = True

    def get_valid_moves(self, row_count, col_count, squares, src_square):
        """
        Get a list of valid moves.
        ::return list: list of squares
        """
        valid_moves = []

        src_row = src_square.get_row()
        src_col = src_square.get_col()

        # Color is white
        if self.color == Color.WHITE:

            # First move
            if self.first_move:
                dest_square = squares[src_row-2][src_col]
                # Not occupied
                if not (dest_square.is_occupied() or squares[src_row-1][src_col].is_occupied()):
                    valid_moves.append(dest_square)

            # Forwards
            # Within bounds
            if (0 <= src_row-1 <= row_count-1):
                dest_square = squares[src_row-1][src_col]
                # Not occupied
                if not dest_square.is_occupied():
                    valid_moves.append(dest_square)

            # Diagonal
            # Within bounds
            if (0 <= src_row-1 <= row_count-1 and 0 <= src_col-1 <= col_count-1):
                dest_square = squares[src_row-1][src_col-1]
                # Occupied
                if dest_square.is_occupied():
                    # Not the same color
                    if not self.color == dest_square.get_piece().get_color():
                        valid_moves.append(dest_square)
            if (0 <= src_row-1 <= row_count-1 and 0 <= src_col+1 <= col_count-1):
                dest_square = squares[src_row-1][src_col+1]
                # Occupied
                if dest_square.is_occupied():
                    # Not the same color
                    if not self.color == dest_square.get_piece().get_color():
                        valid_moves.append(dest_square)

        # Color is black
        else:

            # First move
            if self.first_move:
                dest_square = squares[src_row+2][src_col]
                # Not occupied
                if not (dest_square.is_occupied() or squares[src_row+1][src_col].is_occupied()):
                    valid_moves.append(dest_square)

            # Forwards
            # Within bounds
            if (0 <= src_row+1 <= row_count-1):
                dest_square = squares[src_row+1][src_col]
                # Not occupied
                if not dest_square.is_occupied():
                    valid_moves.append(dest_square)

            # Diagonal
            # Within bounds
            if (0 <= src_row+1 <= row_count-1 and 0 <= src_col-1 <= col_count-1):
                dest_square = squares[src_row+1][src_col-1]
                # Occupied
                if dest_square.is_occupied():
                    # Not the same color
                    if not self.color == dest_square.get_piece().get_color():
                        valid_moves.append(dest_square)
            if (0 <= src_row+1 <= row_count-1 and 0 <= src_col+1 <= col_count-1):
                dest_square = squares[src_row+1][src_col+1]
                # Occupied
                if dest_square.is_occupied():
                    # Not the same color
                    if not self.color == dest_square.get_piece().get_color():
                        valid_moves.append(dest_square)

        return valid_moves
