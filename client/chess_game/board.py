import pygame

from client.chess_game.square import Square
from client.chess_game.pieces import Color, King, Queen, Bishop, Knight, Rook, Pawn


class Board:

    def __init__(self):
        self.row_count = 8
        self.col_count = 8

        self.board_rect = None

        self.squares = [[Square(row, col) for col in range(self.col_count)]
                        for row in range(self.row_count)]

    def get_square(self, x, y):
        """
        Get the square at the specified position.
        ::param x: x position
        ::param y: y position
        """
        for row in range(self.row_count):
            for col in range(self.col_count):
                if self.squares[row][col].is_within_bounds(x, y):
                    return self.squares[row][col]

        return None

    def reset(self):
        """
        Reset the board.
        """
        # Remove pieces
        for row in range(self.row_count):
            for col in range(self.col_count):
                if self.squares[row][col].is_occupied():
                    self.squares[row][col].remove_piece()

        # Add pieces
        self.squares[0][0].add_piece(Rook(Color.BLACK))
        self.squares[0][1].add_piece(Knight(Color.BLACK))
        self.squares[0][2].add_piece(Bishop(Color.BLACK))
        self.squares[0][3].add_piece(Queen(Color.BLACK))
        self.squares[0][4].add_piece(King(Color.BLACK))
        self.squares[0][5].add_piece(Bishop(Color.BLACK))
        self.squares[0][6].add_piece(Knight(Color.BLACK))
        self.squares[0][7].add_piece(Rook(Color.BLACK))
        self.squares[1][0].add_piece(Pawn(Color.BLACK))
        self.squares[1][1].add_piece(Pawn(Color.BLACK))
        self.squares[1][2].add_piece(Pawn(Color.BLACK))
        self.squares[1][3].add_piece(Pawn(Color.BLACK))
        self.squares[1][4].add_piece(Pawn(Color.BLACK))
        self.squares[1][5].add_piece(Pawn(Color.BLACK))
        self.squares[1][6].add_piece(Pawn(Color.BLACK))
        self.squares[1][7].add_piece(Pawn(Color.BLACK))

        self.squares[7][0].add_piece(Rook(Color.WHITE))
        self.squares[7][1].add_piece(Knight(Color.WHITE))
        self.squares[7][2].add_piece(Bishop(Color.WHITE))
        self.squares[7][3].add_piece(Queen(Color.WHITE))
        self.squares[7][4].add_piece(King(Color.WHITE))
        self.squares[7][5].add_piece(Bishop(Color.WHITE))
        self.squares[7][6].add_piece(Knight(Color.WHITE))
        self.squares[7][7].add_piece(Rook(Color.WHITE))
        self.squares[6][0].add_piece(Pawn(Color.WHITE))
        self.squares[6][1].add_piece(Pawn(Color.WHITE))
        self.squares[6][2].add_piece(Pawn(Color.WHITE))
        self.squares[6][3].add_piece(Pawn(Color.WHITE))
        self.squares[6][4].add_piece(Pawn(Color.WHITE))
        self.squares[6][5].add_piece(Pawn(Color.WHITE))
        self.squares[6][6].add_piece(Pawn(Color.WHITE))
        self.squares[6][7].add_piece(Pawn(Color.WHITE))

    def set_rect(self, board_rect):
        """
        Set the board rect.
        ::param board_rect: the board rect
        """
        self.board_rect = board_rect

        self.set_square_rect(self.board_rect)

    def set_square_rect(self, board_rect):
        """
        Set the square rect relative to board rect.
        ::param board_rect: the board rect
        """
        square_width = board_rect.width//self.row_count
        square_height = board_rect.height//self.col_count

        for row in range(self.row_count):
            for col in range(self.col_count):
                square_rect = pygame.Rect((board_rect.left+square_width*col,
                                           board_rect.top+square_width*row), (square_width, square_height))
                self.squares[row][col].set_rect(square_rect)

    def is_within_bounds(self, x, y):
        """
        Check if position is within the board bounds.
        ::param x: x position
        ::param y: y position
        ::return bool: True if position within board bounds, else False
        """
        return (self.board_rect.left < x < self.board_rect.right and self.board_rect.top < y < self.board_rect.bottom)

    def draw(self, surface, valid_moves, previous_move):
        """
        Draw the board to the screen's surface.
        ::param surface: display surface to draw on
        ::param valid_moves: player valid moves
        ::param previous_move: opposing player previous move
        """
        lightBrown = (217, 179, 140)
        darkBrown = (191, 128, 64)
        green = (0, 255, 0)
        red = (255, 0, 0)

        # Draw each square
        for row in range(self.row_count):
            for col in range(self.col_count):

                # Get the square
                square = self.squares[row][col]

                # Get the square's color
                if square in valid_moves:
                    square_color = green
                elif previous_move and square in previous_move:
                    square_color = red
                else:
                    square_color = lightBrown if (
                        row+col) % 2 == 0 else darkBrown

                # Draw the square
                square.draw(surface, square_color)
