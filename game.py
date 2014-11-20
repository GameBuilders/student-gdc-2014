import pygame

#Game class. Keeps track of everything we need to know about the game state (players, map, enemies, powerups, etc.).
class Game():
    # Constructor. Initialize any game objects.
    def __init__(self):
        pass
    
    # Render the current state of the game.
    def render(self):
        screen = pygame.display.get_surface()
    
    # Update the state of the game.
    # delta: Time passed (in seconds) since the previous frame.
    def update(self, delta):
        pass