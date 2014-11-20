import pygame
from scene import *

# A simple class for managing scenes and interactions between them.
class SceneManager():
    # SceneManager constructor
    def __init__(self):
        self.current_scene = None
        
        self.scenes = dict()
    
    # Adds a scene to the scene manager with the given name.
    def add_scene(self, scene_name, scene):
        self.scenes[scene_name] = scene
    
    # Sets the current scene to the scene with the given name.
    def set_scene(self, scene_name):
        self.current_scene = self.scenes[scene_name]
    
    # Returns the current scene.
    def get_scene(self):
        return self.current_scene
