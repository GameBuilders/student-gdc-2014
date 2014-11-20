import pygame
import sys
import os
from game import *

def main():
    # Initialize Pygame
    pygame.init()

    clock = pygame.time.Clock()

    game = Game()

    # Create the window
    size = (1024, 768)
    screen = pygame.display.set_mode(size)

    # Set the window title
    pygame.display.set_caption("Student GDC")

    # Main game loop
    running = True
    while running:
        # Time since last frame (in seconds)
        delta = clock.tick() / 1000.0
    
        # Handle any Pygame events waiting for us
        for event in pygame.event.get():
            # Quit if the user closes the window
            if event.type == pygame.QUIT:
                running = False
        
        # Update the game according to the time passed since last frame
        game.update(delta)
        
        # Clear the screen before rendering
        screen.fill((0, 0, 0))
        
        # Render the game!
        game.render()
        
        # Tell Pygame to swap the screen buffers
        pygame.display.flip()
        
if __name__ == '__main__':
    main()