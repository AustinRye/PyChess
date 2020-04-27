class Square:

    def __init__(self):
        self.piece = None

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

    def replace_piece(self, newPiece):
        """
        Replace the piece on the square.
        ::param newPiece: piece to add to the square
        ::return Piece: piece removed from the square
        """
        oldPiece = self.piece
        self.piece = newPiece
        return oldPiece

    def remove_piece(self):
        """
        Remove the piece from the square.
        ::return Piece: piece removed from the square
        """
        piece = self.piece
        self.piece = None
        return piece

    def is_occupied(self):
        """
        Check if square is occupied.
        ::return bool: True if square is occupied by a piece, False if not
        """
        return (not self.piece == None)
