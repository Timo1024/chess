from .chess_piece import ChessPiece

class Rook(ChessPiece):
    def __init__(self, color):
        super().__init__(color)

    def get_valid_moves(self, board, position):
        # Return a list of valid moves for a pawn at the given position
        y, x = position
        moves = []

        # check the row
        for i in range(8):
            if board[y][i] == None or board[y][i].get_color() != self.color:
                # check if there is another piece in the way
                is_blocked = False
                if i > x:
                    for j in range(x+1, i):
                        if board[y][j] != None:
                            is_blocked = True
                elif i < x:
                    for j in range(i+1, x):
                        if board[y][j] != None:
                            is_blocked = True
                if not is_blocked:
                    moves.append((y, i))
        
        # check the column
        for i in range(8):
            if board[i][x] == None or board[i][x].get_color() != self.color:
                # check if there is another piece in the way
                is_blocked = False
                if i > y:
                    for j in range(y+1, i):
                        if board[j][x] != None:
                            is_blocked = True
                elif i < y:
                    for j in range(i+1, y):
                        if board[j][x] != None:
                            is_blocked = True
                if not is_blocked:
                    moves.append((i, x))

        return moves

    def get_image(self):
        # Return the image of the pawn
        return("Rook")
    
    def get_color(self):
        return self.color
    
    def is_pawn(self):
        return False