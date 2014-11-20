import pygame
from spritesheet import *

# Pidgeon class. Stores pidgeon attack and rendering information.
class Pidgeon():
    # Constructor. Loads pidgeon assets
    def __init__(self, type):
        img_path = None
        if (type == 0):
            img_path = os.path.join('assets', 'pidgeon_anim.png')

        self.spritesheet = Spritesheet(img_path, 64, 64)
        
    # Render the pidgeon
    def render(self, position):
        sprite = self.spritesheet.get_sprite(0)
    
        screen = pygame.display.get_surface()
        screen.blit(self.sprite, position)
