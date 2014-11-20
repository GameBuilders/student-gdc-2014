import pygame
from pidgeon import *
from config import *

# Player class. Keeps track of everything we need to know about a player.
class Player():
    # Constructor. Initialize any player variables.
    def __init__(self):
        self.position = (0, Config.HEIGHT/2)
        self.main_pidgeon = Pidgeon(0) # load starting pidgeon
        self.pidgeons = [self.main_pidgeon]
        self.speed = 10
    
    # Sets the control scheme for this player.
    def set_controls(self):
        pass
        #self.control_forward = 
    
    # Render the current state of the player.
    def render(self):
        self.main_pidgeon.render(self.position)
    
    # Update the state of the player.
    # delta: Time passed (in seconds) since the previous frame.
    def update(self, delta):
        keys_pressed = pygame.key.get_pressed()
        if (keys_pressed[K_w]):
            self.position = (self.position[0], self.position[1] - delta * self.speed)
        if (keys_pressed[K_s]):
            self.position = (self.position[0], self.position[1] + delta * self.speed)
        if (keys_pressed[K_a]):
            self.position = (self.position[0] - delta * self.speed, self.position[1])
        if (keys_pressed[K_d]):
            self.position = (self.position[0] + delta * self.speed, self.position[1])