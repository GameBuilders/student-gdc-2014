import pygame
from config import *
from entity import *

class Enemy(Entity):

    def __init__(self, sprite, y):

        x = Config.WIDTH + 32
        self.speed = 200
        
        Entity.__init__(sprite, x, y)
    
    def update(self, delta, game_scene):
        pass