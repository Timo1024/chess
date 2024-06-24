import pygame
from game import Game

def main():
    pygame.init()

    # Set up some constants
    WIDTH, HEIGHT = 800, 800  # Window size
    FPS = 20  # Frames per second

    # Set up the display
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Set up the clock
    clock = pygame.time.Clock()

    # Create a game instance
    game = Game()

    # Game loop
    running = True
    turn_over = False
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Add more event handlers as needed
            # e.g., mouse clicks, key presses etc.

            # handle mouse click events on the board
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x = pos[0] // 100
                y = pos[1] // 100
                print("Click ", pos, "Grid coordinates: ", x, y)

                if(game.get_marked_square() == (x, y)):
                    game.set_marked_square(None)
                    continue

                if game.get_marked_square() is not None:
                    # move the piece
                    valid_moves = game.get_possible_moves()
                    if valid_moves is not None:
                        if (y, x) in valid_moves:
                            # check if move is en passant to delete the captured pawn
                            if game.board.board[y][x] is None and game.board.board[game.get_marked_square()[1]][x] is not None and game.board.board[game.get_marked_square()[1]][x].is_pawn() and abs(game.get_marked_square()[1] - y) == 1 and abs(game.get_marked_square()[0] - x) == 1:
                                game.board.board[game.get_marked_square()[1]][x] = None

                            # handle move when pawn reaches the end of the board



                            
                            game.board.execute_move(game.get_marked_square(), (x, y))
                            game.set_last_move_en_passant(game.get_marked_square(), (x, y))
                            game.set_marked_square(None)
                            turn_over = True
                            continue

                # highlight the clicked square
                game.set_marked_square((x, y))
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x * 100, y * 100, 100, 100))

        # Update the game state
        if turn_over:
            game.update()
            turn_over = False

        # Draw everything
        game.draw(screen)

        # Flip the display
        pygame.display.flip()

    pygame.quit()

main()