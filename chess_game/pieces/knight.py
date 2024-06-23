from .chess_piece import ChessPiece

class Knight(ChessPiece):
    def __init__(self, color):
        super().__init__(color)

    def get_valid_moves(self, board, position):
        # Return a list of valid moves for a pawn at the given position
        y, x = position
        moves = []

        possible_moves_relative = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for move in possible_moves_relative:
            new_y = y + move[0]
            new_x = x + move[1]
            if new_y >= 0 and new_y < 8 and new_x >= 0 and new_x < 8:
                if board[new_y][new_x] == None or board[new_y][new_x].get_color() != self.color:
                    moves.append((new_y, new_x))
        return moves

    def get_image(self):
        # Return the image of the pawn
        return("Knight")
    
    def get_color(self):
        return self.color
    
    def is_pawn(self):
        return False