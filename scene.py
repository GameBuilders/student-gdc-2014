import pygame

# Represents a single scene in the game.
class Scene():
    # Scene constructor. Receives a Game reference.
    def __init__(self, game):
        # Store a reference to the Game so we can access it.
        self.game = game
    
    # Renders the scene according to its current state.
    def render(self, screen):
        pass
    
    # Updates the scene according to time passed since last update.
    def update(self, delta):
        pass