import pygame
import sys
import os
from game import *
from datetime import datetime

def main():
    # Initialize Pygame
    pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
    pygame.init()

    clock = pygame.time.Clock()

    # Create the window
    size = (1024, 768)
    screen = pygame.display.set_mode(size)

    # Set the window title
    pygame.display.set_caption("Pigeon Rangers")

    music = pygame.mixer.Sound(os.path.join('assets','sounds','muzakfinal.ogg'))  #load music
    music.play(-1)
    
    game = Game()

    # Main game loop
    while game.running:
        # Time since last frame (in seconds)
        delta = clock.tick() / 1000.0
    
        # Handle any Pygame events waiting for us
        for event in pygame.event.get():
            # Quit if the user closes the window
            if event.type == pygame.QUIT:
                game.running = False
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_p):
                    date = datetime.now().date().isoformat()
                    time = datetime.now().time().isoformat()
                    pygame.image.save(screen, "screenshot_" + date + "_" + time + ".png")
        
        # Update the game according to the time passed since last frame
        game.update(delta)
        
        # Clear the screen before rendering
        screen.fill((0, 0, 0))
        
        # Render the game!
        game.render(screen)
        
        # Tell Pygame to swap the screen buffers
        pygame.display.flip()
        
if __name__ == '__main__':
    main()