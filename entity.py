import pygame
from config import *

# Entity class. Keeps track of everything we need to know about an entity.
class Entity():

    # Constructor. Initialize any player variables.
    def __init__(self, sprite, x, y, t):
        self.sprite = sprite
        self.x = x
        self.y = y
        self.state = 0
        self.type = t
        
    
    # Render the entity.
    def render(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
    
    # Update the state of the entity.
    # delta: Time passed (in seconds) since the previous frame.
    def update(self, delta, player):
        rect = pygame.Rect(self.x, self.y, self.sprite.get_width(), self.sprite.get_height())
        if rect.colliderect(player.get_rect()):
            # Kill the player!
            player.die()

        if self.type == 3:#Chasing spike.
            difference = player.position[1] - 50 - self.y
            self.y += delta * 135 * (1 if difference > 10 else (-1 if difference < -10 else 0))
        
        # Check for player projectiles
        proj_to_remove = []
        for proj in player.projectiles:
            if rect.collidepoint(proj.x, proj.y):
                proj_to_remove.append(proj)
        for proj in proj_to_remove:
            player.projectiles.remove(proj)