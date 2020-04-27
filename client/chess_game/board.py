import pygame

from client.chess_game.square import Square
from client.chess_game.pieces import Color, King, Queen, Bishop, Knight, Rook, Pawn


class Board:

    def __init__(self):
        self.rowCount = 8
        self.colCount = 8

        self.squares = [[Square() for _ in range(self.colCount)]
                        for _ in range(self.rowCount)]

    def reset(self):
        """
        Reset the board.
        """
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

    def draw(self, surface, board_rect):
        """
        Draw the board to the screen's surface.
        ::param surface: display surface to draw on
        ::param board_rect: the board rect size
        """
        lightBrown = (217, 179, 140)
        darkBrown = (191, 128, 64)

        square_width = board_rect.width//self.rowCount
        square_height = board_rect.height//self.colCount

        piece_width = square_width - 10
        piece_height = square_height - 10

        # Draw each square
        for row in range(self.rowCount):
            for col in range(self.colCount):

                square = self.squares[row][col]

                # Draw the square
                square_color = lightBrown if (row+col) % 2 == 0 else darkBrown
                square_rect = pygame.Rect(
                    (board_rect.left+square_width*col, board_rect.top+square_width*row), (square_width, square_height))
                pygame.draw.rect(surface, square_color, square_rect)

                # Draw the square's piece if occupied
                if square.is_occupied():
                    image = pygame.transform.scale(
                        square.get_piece().get_image(), (piece_width, piece_height))
                    image_rect = ((board_rect.left+col*square_width+(square_width-piece_width)/2, board_rect.top +
                                   row*square_height+(square_height-piece_height)/2), (piece_width, piece_height))
                    surface.blit(image, image_rect)
