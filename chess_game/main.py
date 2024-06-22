import pygame
from game import Game

def main():
    pygame.init()

    # Set up some constants
    WIDTH, HEIGHT = 800, 800  # Window size
    FPS = 60  # Frames per second

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

        # Update the game state
        game.update()

        # Draw everything
        game.draw(screen)

        # Flip the display
        pygame.display.flip()

    pygame.quit()

main()