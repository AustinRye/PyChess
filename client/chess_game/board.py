import pygame

from client.chess_game.square import Square


class Board:

    def __init__(self):
        self.rowCount = 8
        self.colCount = 8

        self.squares = [[Square() for _ in range(self.colCount)]
                        for _ in range(self.rowCount)]

    def draw(self, surface, board_rect):
        """
        Draw the board to the screen's surface.
        ::param surface: display surface to draw on
        ::param board_rect: the board rect size
        """
        lightBrown = (217, 179, 140)
        darkBrown = (191, 128, 64)

        square_width = board_rect.width/self.rowCount
        square_height = board_rect.height/self.colCount

        # Draw each square
        for row in range(self.rowCount):
            for col in range(self.colCount):

                square = self.squares[row][col]

                square_color = lightBrown if (row+col) % 2 == 0 else darkBrown

                square_rect = pygame.Rect(
                    (board_rect.left+square_width*col, board_rect.top+square_width*row), (square_width, square_height))

                pygame.draw.rect(surface, square_color, square_rect)
