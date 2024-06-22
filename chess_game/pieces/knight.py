from .chess_piece import ChessPiece

class Knight(ChessPiece):
    def __init__(self, color):
        super().__init__(color)

    def get_valid_moves(self, board, position):
        # Return a list of valid moves for a pawn at the given position
        pass

    def get_image(self):
        # Return the image of the pawn
        return("Knight")
    
    def get_color(self):
        return self.color
    
    def is_pawn(self):
        return False