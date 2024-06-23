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
                            game.board.execute_move(game.get_marked_square(), (x, y))
                            game.set_marked_square(None)
                            continue

                # highlight the clicked square
                game.set_marked_square((x, y))
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x * 100, y * 100, 100, 100))

        # Update the game state
        game.update()

        # Draw everything
        game.draw(screen)

        # Flip the display
        pygame.display.flip()

    pygame.quit()

main()