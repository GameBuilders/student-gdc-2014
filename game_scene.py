from scene import *
from config import *
from player import *
from projectile import *
from progressbar import *
from cooldown import *
from level import *

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

        self.cooldownicon= CooldownIcon()

        Scene.__init__(self, game)
        self.lives = 3
        self.lives_sprite= pygame.image.load('assets/heart.png')
        self.lives_rect= self.lives_sprite.get_rect()
        self.level = Level(1)

    # Renders the scene according to its current state.
    def render(self, screen):

        # render player projectiles
        self.level.render(screen)
        for p in self.player_projectiles:
            p.render(screen)

        # Render normal state
        self.cooldownicon.render(screen)
        self.player.render()
        self.ProgressBar.render(screen)

        for i in range(self.lives):
            screen.blit(self.lives_sprite,(10+self.lives_rect.left+(i*40),50))
        
          
    # Updates the scene according to the time passed since last update.
    def update(self, delta):
        self.level.update(delta)
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


        self.ProgressBar.update(delta)
        self.cooldownicon.update(delta)

