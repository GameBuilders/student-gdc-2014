import pygame
from config import *

class CooldownIcon():
    
    def __init__(self):
        self.fireball_sprite = pygame.image.load('assets/fireball_icon.png')
        self.fireball_rect= self.fireball_sprite.get_rect()
        self.font = pygame.font.Font(None, 36)
        self.cooldown=20
        self.text = self.font.render(str(self.cooldown), 1, (255, 10, 10))
        self.textpos = self.text.get_rect(centerx=Config.WIDTH/2)
        
    def render(self, screen):
        # Render normal state
        
        screen.blit(self.fireball_sprite,(10+self.fireball_rect.left,Config.HEIGHT-80))
        if int(self.cooldown) > 0: 
            self.size=self.font.size(str(int(self.cooldown)))
            screen.blit(self.text, (40+self.fireball_rect.left-self.size[0]/2,Config.HEIGHT-60))
        
    
    # Updates the scene according to the time passed since last update.
    def update(self, delta):
        self.cooldown-=delta
        self.text = self.font.render(str(int(self.cooldown)), 1, (255, 10, 10))
        
                
        pass
        