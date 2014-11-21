import pygame
from config import *

# Player class. Keeps track of everything we need to know about a player.
class Entity():

    # Constructor. Initialize any player variables.
    def __init__(self):
    
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
        
        # Update pidgeon
        self.main_pidgeon.update(delta)
