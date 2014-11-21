import pygame
from config import *
from entity import *

class Enemy(Entity):

    def __init__(self, my_y):

        self.position = [Config.WIDTH + 32, my_y]
        self.speed = 200
    
    def set_controls(self):
        pass
    
    def update(self, delta):
        keys_pressed = pygame.key.get_pressed()

        self.position