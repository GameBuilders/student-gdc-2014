from scene import *
from config import *
from player import *
from projectile import *
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
        self.player_projectiles = []
        self.player_projectile_cooldown = 0.5
        Scene.__init__(self, game)
        
    # Renders the scene according to its current state.
    def render(self, screen):

        # render player projectiles
        for p in self.player_projectiles:
            p.render(screen)
        
        self.player.render()
        self.ProgressBar.render(screen)
        
          
    # Updates the scene according to the time passed since last update.
    def update(self, delta):
        self.player.update(delta)

        self.player_projectile_cooldown -= delta
        if (self.player_projectile_cooldown < 0.0):
            self.player_projectile_cooldown = 0.5
            self.player_projectiles.append(Projectile(self.player.position[0], self.player.position[1], 400.0, 0.0))

        # update projectiles
        for p in self.player_projectiles:
            p.update(delta)
            # remove projectiles that are off screen
            if (p.x > Config.WIDTH or p.y > Config.HEIGHT or p.y < 0.0):
                self.player_projectiles.remove(p)

class ProgressBar():
    
    def __init__(self,level):
        self.level = level
        self.progressbar_sprite = pygame.image.load('assets/progress_bar.png')
        self.progressindicator_sprite = pygame.image.load('assets/progress_indicator.png')
        self.progressindicator_rect= self.progressindicator_sprite.get_rect()
        self.progressbar_rect= self.progressbar_sprite.get_rect()
        levellength = 2000
        progress = 800
        progressRatio = progress/levellength
    def render(self, screen):
        # Render normal state

        screen.blit(self.progressbar_sprite,self.progressbar_rect)
        screen.blit(self.progressindicator_sprite,self.progressindicator_rect)
        
    
    # Updates the scene according to the time passed since last update.
    def update(self, delta):
        progressindicator_rect.left= Config.WIDTH*progressRatio
        