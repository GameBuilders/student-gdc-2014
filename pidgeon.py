import pygame
import os
from spritesheet import *

# Pidgeon class. Stores pidgeon attack and rendering information.
class Pidgeon():
    # Constructor. Loads pidgeon assets
    def __init__(self, type):
        self.type = type
        self.frame_idx = 0
        self.frame_rate = 12.0
        self.frame_time_left = 1 / self.frame_rate
    
        self.spritesheet = Spritesheet(os.path.join('assets', 'pidgeon_anim.png'), 64, 64)
        
    # Render the pidgeon
    def render(self, position):
        frame_offset = self.type * 8
        sprite = self.spritesheet.get_sprite(frame_offset + self.frame_idx)
    
        screen = pygame.display.get_surface()
        screen.blit(sprite, position)

    def update(self, delta):
        self.frame_time_left -= delta
        if self.frame_time_left <= 0:
            self.frame_idx += 1
            self.frame_time_left += 1 / self.frame_rate
        
        if self.frame_idx >= 8:
            self.frame_idx = 0