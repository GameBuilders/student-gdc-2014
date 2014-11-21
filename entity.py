import pygame
import math
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
        if (self.type == 4):#spiraling spike
            self.center_x = x
            self.center_y = y
            self.radius = 0
            self.radians = 0
        
    
    # Render the entity.
    def render(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
    
    # Update the state of the entity.
    # delta: Time passed (in seconds) since the previous frame.
    def update(self, delta, player):

        rect = pygame.Rect(self.x, self.y, self.sprite.get_width(), self.sprite.get_height())

        if (self.type > -1):
            
            if rect.colliderect(player.get_rect()):
                # Kill the player!
                player.die()

            if self.type == 3 or self.type == 1:#Chasing spike or bat.
                difference = player.position[1] - 50 - self.y
                self.y += delta * 90 * (1 if difference > 10 else (-1 if difference < -10 else 0))
            if self.type ==  4:#spiraling spike
                self.center_x -= Config.SCROLL_SPEED * delta
                self.radius += delta * 30
                self.radians += delta * math.pi / self.radius * 120
                self.x = self.center_x + self.radius * math.cos(self.radians)
                self.y = self.center_y + self.radius * math.sin(self.radians)
            # Check for player projectiles
            proj_to_remove = []
            for proj in player.projectiles:
                if rect.collidepoint(proj.x, proj.y):
                    proj_to_remove.append(proj)
            for proj in proj_to_remove:
                player.projectiles.remove(proj)

        else:

            if rect.colliderect(player.get_rect()):
                player.found_bird = True