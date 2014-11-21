import pygame
from config import *
import os
from spritesheet import *

class CooldownIcon():
    
    def __init__(self, type):
        img_path = os.path.join('assets', 'icons.png')
        self.spritesheet = Spritesheet(img_path, 64, 64)
        self.sprite = self.spritesheet.get_sprite(type)
        self.rect = self.sprite.get_rect()

        self.position = (10 + (type*(self.rect.width+10)), Config.HEIGHT-80)

        self.font = pygame.font.Font(None, 36)
        self.cooldown=20
        self.text = self.font.render(str(self.cooldown), 1, (255, 10, 10))
        self.textpos = self.text.get_rect(centerx=Config.WIDTH/2)
        
    def render(self, screen):
        # Render normal state
        
        screen.blit(self.sprite,self.position)
        if int(self.cooldown) > 0: 
            self.size=self.font.size(str(int(self.cooldown)))
            screen.blit(self.text, (self.position[0]+30-self.size[0]/2,Config.HEIGHT-60))
        
    
    # Updates the scene according to the time passed since last update.
    def update(self, delta):
        self.cooldown-=delta
        self.text = self.font.render(str(int(self.cooldown)), 1, (255, 10, 10))
        
                
        pass
        