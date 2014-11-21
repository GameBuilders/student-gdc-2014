import pygame
from config import *

# Entity class. Keeps track of everything we need to know about an entity.
class Entity():

    # Constructor. Initialize any player variables.
    def __init__(self, sprite, x, y):
        self.sprite = sprite
        self.x = x
        self.y = y
    
    # Render the entity.
    def render(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
    
    # Update the state of the player.
    # delta: Time passed (in seconds) since the previous frame.
    def update(self, delta):
        pass