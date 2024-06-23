from .chess_piece import ChessPiece

class Bishop(ChessPiece):
    def __init__(self, color):
        super().__init__(color)

    def get_valid_moves(self, board, position):
        # Return a list of valid moves for a pawn at the given position
        y, x = position
        moves = []
        
        for i in range(8):
            if y + i < 8 and x + i < 8:
                if board[y+i][x+i] == None or board[y+i][x+i].get_color() != self.color:
                    # check if there is another piece in the way
                    is_blocked = False
                    if i > 0:
                        for j in range(1, i):
                            if board[y+j][x+j] != None:
                                is_blocked = True
                    if not is_blocked:
                        moves.append((y+i, x+i))
            if y + i < 8 and x - i >= 0:
                if board[y+i][x-i] == None or board[y+i][x-i].get_color() != self.color:
                    # check if there is another piece in the way
                    is_blocked = False
                    if i > 0:
                        for j in range(1, i):
                            if board[y+j][x-j] != None:
                                is_blocked = True
                    if not is_blocked:
                        moves.append((y+i, x-i))
            if y - i >= 0 and x + i < 8:
                if board[y-i][x+i] == None or board[y-i][x+i].get_color() != self.color:
                    # check if there is another piece in the way
                    is_blocked = False
                    if i > 0:
                        for j in range(1, i):
                            if board[y-j][x+j] != None:
                                is_blocked = True
                    if not is_blocked:
                        moves.append((y-i, x+i))
            if y - i >= 0 and x - i >= 0:
                if board[y-i][x-i] == None or board[y-i][x-i].get_color() != self.color:
                    # check if there is another piece in the way
                    is_blocked = False
                    if i > 0:
                        for j in range(1, i):
                            if board[y-j][x-j] != None:
                                is_blocked = True
                    if not is_blocked:
                        moves.append((y-i, x-i))
        return moves

    def get_image(self):
        # Return the image of the pawn
        return("Bishop")
    
    def get_color(self):
        return self.color
    
    def is_pawn(self):
        return False