import pygame
from config import *

class Enemy():
    def __init__(self, spritesheet, y):

        x = Config.WIDTH + 32
        self.speed = 200
        
        Entity.__init__(sprite, x, y)
    
    def update(self, delta, game_scene):
        pass