import pygame
from board import Board

class Game:
    def __init__(self):
        self.board = Board()

    def update(self):
        # Update the game state here
        # This could include things like checking for check/checkmate, moving pieces, etc.
        pass

    def draw(self, screen):
        # Draw the game state to the screen here
        # This could include things like drawing the board, the pieces, etc.
        # Define some constants
        BOARD_COLOR_1 = (233, 236, 239)  # Light square color
        BOARD_COLOR_2 = (125, 135, 150)  # Dark square color
        SQUARE_SIZE = 100  # Size of each square on the board

        # Draw the board
        for row in range(8):
            for col in range(8):
                color = BOARD_COLOR_1 if (row + col) % 2 == 0 else BOARD_COLOR_2
                pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        # draw small numbers for rows and columns to help with debugging
        for i in range(8):
            font = pygame.font.Font(None, 15)
            text = font.render(str(i), True, (0, 0, 0))
            text_rect_r = text.get_rect(center=(10, i * SQUARE_SIZE + SQUARE_SIZE // 2))
            text_rect_c = text.get_rect(center=(i * SQUARE_SIZE + SQUARE_SIZE // 2, 10))
            screen.blit(text, text_rect_r)
            screen.blit(text, text_rect_c)

        for row in range(8):
            for col in range(8):
                piece = self.board.board[row][col]
                if piece is not None:
                    # This is where you draw the piece

                    if(piece.get_color() == "black"):
                        color = (0, 0, 0)
                    else:
                        color = (255, 255, 255)

                    text = pygame.font.SysFont(None, 24).render(piece.get_image(), True, color)
                    text_rect = text.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2))
                    screen.blit(text, text_rect)