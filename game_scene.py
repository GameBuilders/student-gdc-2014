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
        
        # Call the base class's constructor
        self.player = Player()
        self.player_projectiles = []
        self.player_projectile_cooldown = 0.5

        self.cooldownicon  = CooldownIcon(0)
        self.cooldownicon2 = CooldownIcon(1)
        self.cooldownicon3 = CooldownIcon(2)
        self.cooldownicon4 = CooldownIcon(3)

        self.lives_sprite= pygame.image.load('assets/heart.png')
        self.lives_rect= self.lives_sprite.get_rect()
        self.level = Level(1)
        self.ProgressBar = ProgressBar(self.level)
        
        self.enemies = []
        self.obstacles = []

        # sprite initialization
        self.sprite_bullet = pygame.image.load(os.path.join('assets','projectile.png'))
        Scene.__init__(self, game)

    # Renders the scene according to its current state.
    def render(self, screen):

        # render player projectiles
        self.level.render(screen)
        for p in self.player_projectiles:
            p.render(screen)

        for obstacle in self.obstacles:
            obstacle.render(screen)
            
        # Render normal state
        self.cooldownicon.render(screen)
        self.cooldownicon2.render(screen)
        self.cooldownicon3.render(screen)
        self.cooldownicon4.render(screen)
        self.player.render()
        self.ProgressBar.render(screen)

        for i in range(self.player.lives):
            screen.blit(self.lives_sprite,(10+self.lives_rect.left+(i*40),50))
        
          
    # Updates the scene according to the time passed since last update.
    def update(self, delta):
        self.level.update(delta, self)
        self.player.update(delta)
        self.player_projectile_cooldown -= delta
        if (self.player_projectile_cooldown < 0.0):
            self.player_projectile_cooldown = 0.2

            # attack patterns
            if self.player.status == 0:
                self.player_projectiles.append(Projectile(self.player.position[0]+60, self.player.position[1]+32, 400.0, 0.0, self.sprite_bullet))
            if self.player.status == 1:
                self.player_projectiles.append(Projectile(self.player.position[0]+60, self.player.position[1]+32, 400.0, 200.0, self.sprite_bullet))
                self.player_projectiles.append(Projectile(self.player.position[0]+60, self.player.position[1]+32, 400.0, -200.0, self.sprite_bullet))
            if self.player.status == 2:
                self.player_projectiles.append(Projectile(self.player.position[0]+60, self.player.position[1]+32, 400.0, 600.0, self.sprite_bullet))
                self.player_projectiles.append(Projectile(self.player.position[0]+60, self.player.position[1]+32, 400.0, -600.0, self.sprite_bullet))



        # update projectiles
        for p in self.player_projectiles:
            p.update(delta)
            # remove projectiles that are off screen
            if (p.x > Config.WIDTH or p.y > Config.HEIGHT or p.y < 0.0):
                self.player_projectiles.remove(p)

        # update obstacles
        obstacles_to_remove = []
        for obstacle in self.obstacles:
            # Make obstacle move to match map scrolling speed
            obstacle.x -= Config.SCROLL_SPEED * delta
            obstacle.update(delta, self.player)
            
            if obstacle.x < -50:
                obstacles_to_remove.append(obstacle)
        
        for obstacle in obstacles_to_remove:
            self.obstacles.remove(obstacle)

        self.ProgressBar.update(delta)
        self.cooldownicon.update(delta)
        self.cooldownicon2.update(delta)
        self.cooldownicon3.update(delta)
        self.cooldownicon4.update(delta)


