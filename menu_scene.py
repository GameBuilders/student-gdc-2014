from scene import *
from config import *

# A scene sub-class that represents the menu.
class MenuScene(Scene):
    # Scene constructor. Receives a Game reference.
    def __init__(self, game):
        # Menu scene
        self.title_sprite = pygame.image.load('assets/title.png')
        self.how_to_play_sprite = pygame.image.load('assets/how_to_play.png')
        
        # State of the menu. 0 = normal, 1 = how to play
        self.state = 0
        
        # Call the base class's constructor
        Scene.__init__(self, game)
    
    # Renders the scene according to its current state.
    def render(self, screen):
        # Render normal state
        if self.state is 0:
            rect = self.title_sprite.get_rect()
            rect.center = (Config.WIDTH / 2, Config.HEIGHT / 2)
            screen.blit(self.title_sprite, rect)
        
        # Render How to Play state
        elif self.state is 1:
            rect = self.how_to_play_sprite.get_rect()
            rect.center = (Config.WIDTH / 2, Config.HEIGHT / 2)
            screen.blit(self.how_to_play_sprite, rect)
    
    # Updates the scene according to the time passed since last update.
    def update(self, delta):
        pass