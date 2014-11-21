import pygame
from config import *

class Enemy():
    def __init__(self, spritesheet, y):
        self.spritesheet = spritesheet
        self.x = Config.WIDTH + 64
        self.y = y
        
        self.frame = 40
        self.frame_time = 1.0 / 12.0
        
        self.health = 100
    
    def render(self, screen):
        sprite = self.spritesheet.get_sprite(self.frame)
        screen.blit(sprite, (self.x, self.y))
    
    def update(self, delta, player):
        self.frame_time -= delta
        if self.frame_time <= 0:
            self.frame_time += 1.0 / 12.0
            self.frame += 1
        if self.frame >= 43:
            self.frame = 40
        
        rect = pygame.Rect(self.x, self.y, 64, 64)
        if rect.colliderect(player.get_rect()):
            # Kill the player!
            player.die()
        
        # Check for player projectiles
        proj_to_remove = []
        for proj in player.projectiles:
            if rect.collidepoint(proj.x, proj.y):
                proj_to_remove.append(proj)
                self.health -= proj.damage
        for proj in proj_to_remove:
            player.projectiles.remove(proj)
            
        if self.health <= 0:
            return True #true = remove me
        return False