import pygame
from random import randint

from client.chess_game.board import Board
from client.chess_game.player import Player
from client.chess_game.pieces import Color, Pawn


class ChessGame:

    def __init__(self):
        self.board = Board()

        self.player_white = Player(Color.WHITE)
        self.player_black = Player(Color.BLACK)

        self.player_turn = None
        self.legal_moves = []

    def reset(self):
        """
        Reset the chess game.
        """
        self.board.reset()

        self.player_turn = self.player_white if randint(
            0, 1) else self.player_black
        print(f'[TURN] {self.player_turn.get_color()}')

    def next_turn(self):
        self.player_turn = self.player_white if (
            self.player_turn.get_color() == Color.BLACK) else self.player_black
        print(f'[TURN] {self.player_turn.get_color()}')

    def handle_mouse_down(self, x, y):
        """
        Handle mouse down event.
        ::param x: x position
        ::param y: y position
        """
        if self.board.is_within_bounds(x, y):  # Coordinates within board bounds
            square = self.board.get_square(x, y)
            if square.is_occupied():  # Square is occupied
                # Player and piece color are the same
                if self.player_turn.get_color() == square.get_piece().get_color():
                    # Pick up the piece at the selected square
                    self.player_turn.pick_piece(square)
                    self.legal_moves = self.player_turn.get_selected_piece(
                    ).get_legal_moves(self.board.row_count, self.board.col_count, self.board.squares, square)

    def handle_mouse_up(self, x, y):
        """
        Handle mouse up event.
        ::param x: x position
        ::param y: y position
        """
        if self.board.is_within_bounds(x, y):  # Coordinates within board bounds
            square = self.board.get_square(x, y)

            if self.player_turn.get_selected_piece():  # Player has a selected piece
                # Move is legal
                if square in self.legal_moves or len(self.legal_moves) == 0:
                    if square.is_occupied():  # Square is occupied
                        # Player and piece color are not the same
                        if not self.player_turn.get_color() == square.get_piece().get_color():
                            # Replace the piece at the selected square
                            self.player_turn.replace_piece(square)
                            # If pawn, set first move to False
                            if isinstance(square.get_piece(), Pawn):
                                if square.get_piece().first_move == True:
                                    square.get_piece().first_move = False
                            self.next_turn()
                        else:  # Player and piece color are the same
                            self.player_turn.cancel_selected_piece()
                    else:
                        # Square is not the same as the previous square
                        if not self.player_turn.get_previous_square() == square:
                            # Place the piece at the selected square
                            self.player_turn.place_piece(square)
                            # If pawn, set first move to False
                            if isinstance(square.get_piece(), Pawn):
                                if square.get_piece().first_move == True:
                                    square.get_piece().first_move = False
                            self.next_turn()
                        else:  # Square is the same as the previous square
                            self.player_turn.cancel_selected_piece()
                else:  # Move is not legal
                    self.player_turn.cancel_selected_piece()

                # Clear legal moves
                self.legal_moves = []

    def draw(self, surface):
        """
        Draw the chess game to the screen's surface.
        ::param surface: display surface to draw on
        """
        # Draw the board
        self.board.draw(surface, self.legal_moves)

        # Draw the player's selected piece
        if self.player_turn.get_selected_piece():
            self.player_turn.draw_selected_piece(surface)
