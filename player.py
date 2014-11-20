import pygame
from pidgeon import *

# Player class. Keeps track of everything we need to know about a player.
class Player():
    # Constructor. Initialize any player variables.
    def __init__(self):
        self.position = (0, 0)
        self.main_pidgeon = Pidgeon(0) # load starting pidgeon
        self.pidgeons = [self.main_pidgeon]
        pass
    
    # Sets the control scheme for this player.
    def set_controls(self):
        #self.control_forward = 
    
    # Render the current state of the player.
    def render(self, screen):
        #screen = pygame.display.get_surface()
        self.main_pidgeon.render(self.position)
    
    # Update the state of the player.
    # delta: Time passed (in seconds) since the previous frame.
    def update(self, delta):
        pass