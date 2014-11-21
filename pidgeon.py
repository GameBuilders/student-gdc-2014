import pygame
import os
from spritesheet import *

# Pidgeon class. Stores pidgeon attack and rendering information.
class Pidgeon():
    # Constructor. Loads pidgeon assets
    def __init__(self, type):
        self.frame_idx = 0
        self.frame_rate = 12.0
        self.frame_time_left = 1 / self.frame_rate
    
        img_path = None
        if (type == 0):
            img_path = os.path.join('assets', 'pidgeon_anim.png')

        self.spritesheet = Spritesheet(img_path, 64, 64)
        
    # Render the pidgeon
    def render(self, position):
        sprite = self.spritesheet.get_sprite(self.frame_idx)
    
        screen = pygame.display.get_surface()
        screen.blit(sprite, position)

    def update(self, delta):
        self.frame_time_left -= delta
        if self.frame_time_left <= 0:
            self.frame_idx += 1
            self.frame_time_left += 1 / self.frame_rate
        
        if self.frame_idx >= 8:
            self.frame_idx = 0