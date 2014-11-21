from scene import *
from config import *
from player import *
from progressbar import *
from cooldown import *
# A scene sub-class that represents the game.
class GameScene(Scene):
    # Scene constructor. Receives a Game reference.
    def __init__(self, game):
        # game scene
        
        # State of the game. 0 = normal, 1 = how to play
        
        self.state = 0
        self.ProgressBar = ProgressBar(None)
        # Call the base class's constructor
        self.player = Player()
        self.cooldownicon= CooldownIcon()
        Scene.__init__(self, game)
        self.lives = 3
        self.lives_sprite= pygame.image.load('assets/heart.png')
        self.lives_rect= self.lives_sprite.get_rect()
    # Renders the scene according to its current state.
    def render(self, screen):
        # Render normal state
        self.cooldownicon.render(screen)
        self.player.render()
        self.ProgressBar.render(screen)

        for i in range(self.lives):
            screen.blit(self.lives_sprite,(10+self.lives_rect.left+(i*40),50))

        # Render How to Play state
        
          
    # Updates the scene according to the time passed since last update.
    def update(self, delta):
        self.player.update(delta)
        self.ProgressBar.update(delta)
        self.cooldownicon.update(delta)
        pass


