from .chess_piece import ChessPiece

class Pawn(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.en_passant = False

    def get_valid_moves(self, board, position):
        # Return a list of valid moves for a pawn at the given position

        print(str(position))
        
        y, x = position
        moves = []

        if self.color == 'white':
            # White pawns move up
            if y > 0 and board[y - 1][x] is None:
                moves.append((y - 1, x))
            if y == 6 and board[y - 1][x] is None and board[y - 2][x] is None:
                # Double move from starting position
                moves.append((y - 2, x))
            # Capture
            if y > 0 and x > 0 and board[y - 1][x - 1] is not None and board[y - 1][x - 1].color != self.color:
                moves.append((y - 1, x - 1))
            if y > 0 and x < 7 and board[y - 1][x + 1] is not None and board[y - 1][x + 1].color != self.color:
                moves.append((y - 1, x + 1))
            # En passant
            if y == 3 and x > 0 and board[y][x - 1] is not None and board[y - 1][x - 1] is None and board[y][x - 1].color != self.color and board[y][x - 1].is_pawn() and board[y][x - 1].en_passant:
                moves.append((y - 1, x - 1))
        else:
            # Black pawns move down
            if y < 7 and board[y + 1][x] is None:
                moves.append((y + 1, x))
            if y == 1 and board[y + 1][x] is None and board[y + 2][x] is None:
                # Double move from starting position
                moves.append((y + 2, x))
            # Capture
            if y < 7 and x > 0 and board[y + 1][x - 1] is not None and board[y + 1][x - 1].color != self.color:
                moves.append((y + 1, x - 1))
            if y < 7 and x < 7 and board[y + 1][x + 1] is not None and board[y + 1][x + 1].color != self.color:
                moves.append((y + 1, x + 1))
            # En passant
            if y == 4 and x > 0 and board[y][x - 1] is not None and board[y + 1][x - 1] is None and board[y][x - 1].color != self.color and board[y][x - 1].is_pawn() and board[y][x - 1].en_passant:
                moves.append((y + 1, x - 1))

        return moves

    def get_image(self):
        # Return the image of the pawn
        return("Pawn")
    
    def get_color(self):
        return self.color
    
    def is_pawn(self):
        return True
    
    def set_en_passant(self, en_passant):
        self.en_passant = en_passant