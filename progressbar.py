import pygame
from config import *
from level import *
class ProgressBar():
    
    def __init__(self,level):
        self.level=level
        self.progressbar_sprite = pygame.image.load('assets/progress_bar.png')
        self.progressindicator_sprite = pygame.image.load('assets/progress_indicator.png')
        self.progressindicator_rect= self.progressindicator_sprite.get_rect()
        self.progressbar_rect= self.progressbar_sprite.get_rect()
        self.progressbar_rect.centery=22
        self.levellength = self.level.duration
        self.progress = self.level.time
        self.progressRatio = self.progress/self.levellength
    def render(self, screen):
        # Render normal state

        screen.blit(self.progressbar_sprite,self.progressbar_rect)
        screen.blit(self.progressindicator_sprite,self.progressindicator_rect)
        
    
    # Updates the scene according to the time passed since last update.
    def update(self, delta):
        self.levellength = self.level.duration
        self.progress = self.level.time
        self.progressRatio = self.progress/self.levellength
        self.progressindicator_rect.left= Config.WIDTH*self.progressRatio
        pass
        