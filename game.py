import pygame
from scenemanager import *

# Import scenes
from menu_scene import *

# Game class. Keeps track of everything we need to know about the game state (players, map, enemies, powerups, etc.).
class Game():
    # Constructor. Initialize any variables and game objects.
    def __init__(self):
        # Initially the game is running and unpaused.
        self.running = True
        self.paused = False
        
        # Used to manage the various scenes in the game.
        self.scene_manager = SceneManager()
        
        # Add any scenes needed by the game here
        self.scene_manager.add_scene("MenuScene", MenuScene(self))
        
        # Make sure to set the initial scene!
        self.scene_manager.set_scene("MenuScene")
    
    # Pauses the game. Pausing prevents any updates from being done.
    def pause(self):
        self.paused = True
    
    # Unpauses the game. Unpausing allows the game state to be updated.
    def unpause(self):
        self.paused = False
    
    # Render the current state of the game.
    def render(self, screen):
        # Get the current scene
        scene = self.scene_manager.get_scene()
    
        # Render the scene
        scene.render(screen)
    
    # Update the state of the game.
    # delta: Time passed (in seconds) since the previous frame.
    def update(self, delta):
        if self.paused:
            # The game is paused, so don't do any updates!
            return
        
        # Get the current scene
        scene = self.scene_manager.get_scene()

        # Update the scene
        scene.update(delta)