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
        self.game = game
        
        # State of the game. 0 = normal, 1 = how to play
        self.state = 0
        
        # Call the base class's constructor
        self.player = Player()
        #self.player_projectiles = [] # use self.player.projectiles
        self.player_projectile_cooldown = 0.5

        self.cd_icon = [CooldownIcon(0), CooldownIcon(1), CooldownIcon(2), CooldownIcon(3)]

        self.lives_sprite= pygame.image.load('assets/heart.png')
        self.lives_rect= self.lives_sprite.get_rect()
        self.level = Level(1)
        self.ProgressBar = ProgressBar(self.level)
        
        self.enemies = []
        self.obstacles = []

        # sprite initialization
        directory = os.path.join('assets','projectiles')
        self.sprite_b0 = pygame.image.load(os.path.join(directory,'gray.png'))
        self.sprite_b1 = pygame.image.load(os.path.join(directory,'red.png'))
        self.sprite_b2 = pygame.image.load(os.path.join(directory,'blue.png'))
        self.sprite_b3 = pygame.image.load(os.path.join(directory,'purple.png'))
        self.sprite_b4 = pygame.image.load(os.path.join(directory,'jesus.png'))

        Scene.__init__(self, game)

        # game over alpha
        self.alpha_gameover = 0
        self.sprite_gameover = pygame.image.load(os.path.join('assets','lose_screen.png')).convert_alpha()
        self.surface_gameover = pygame.Surface(self.sprite_gameover.get_size(), depth=24)

    # Renders the scene according to its current state.
    def render(self, screen):

        # render player projectiles
        self.level.render(screen)
        for p in self.player.projectiles:
            p.render(screen)

        for obstacle in self.obstacles:
            obstacle.render(screen)
        
        for enemy in self.enemies:
            enemy.render(screen)
            
        # Render normal state
        for i in range(len(self.player.pidgeons) - 1):
            self.cd_icon[i].render(screen)

        self.player.render()
        self.ProgressBar.render(screen)

        # render lives
        for i in range(self.player.lives):
            screen.blit(self.lives_sprite,(10+self.lives_rect.left+(i*40),50))

        # render game over screen
        if (self.player.lives <= 0):
            
            if self.alpha_gameover < 255:
                self.alpha_gameover += 10

            key = pygame.Color('black')
            #self.surface_gameover.fill(key)
            self.surface_gameover.set_colorkey(key)
            self.surface_gameover.blit(self.sprite_gameover, (0,0))
            self.surface_gameover.set_alpha(self.alpha_gameover) 
            screen.fill(pygame.Color('black'))
            screen.blit(self.surface_gameover, (0,0))
            pass

    # Updates the scene according to the time passed since last update.
    def update(self, delta):

        #if (self.player.lives is 2):
        #    self.__init__(self.game)
        if self.player.lives is 0:
            # Restart upon pressing 'R'
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_r]:
                self.__init__(self.game)
        if self.player.lives > 0:

            self.level.update(delta, self)
            self.player.update(delta)
            self.player_projectile_cooldown -= delta
            bullettype = self.player.status

            cap = 0.3
            if bullettype == 0:
                cap = 0.3
            if bullettype == 1:
                cap = 0.2
            if bullettype == 2:
                cap = 0.5
            if bullettype == 3:
                cap = 0.2
            if bullettype == 4:
                cap = 0.1

            # if you can shoot
            if (self.player_projectile_cooldown < 0.0):
                self.player_projectile_cooldown = cap

                # attack patterns
                if bullettype == 0:
                    self.player.projectiles.append(Projectile(self.player.position[0]+60, self.player.position[1]+32, 400.0, 0.0, self.sprite_b0))
                if bullettype == 1:
                    self.player.projectiles.append(Projectile(self.player.position[0]+60, self.player.position[1]+32, 400.0, -200.0, self.sprite_b1))
                    self.player.projectiles.append(Projectile(self.player.position[0]+60, self.player.position[1]+32, 400.0, 200.0, self.sprite_b1))
                if bullettype == 2:
                    self.player.projectiles.append(Projectile(self.player.position[0]+60, self.player.position[1]+32, 600.0, 150.0, self.sprite_b2))
                    self.player.projectiles.append(Projectile(self.player.position[0]+60, self.player.position[1]+32, 600.0, 0.0, self.sprite_b2))
                    self.player.projectiles.append(Projectile(self.player.position[0]+60, self.player.position[1]+32, 600.0, 300.0, self.sprite_b2))
                    self.player.projectiles.append(Projectile(self.player.position[0]+60, self.player.position[1]+32, 600.0, -150.0, self.sprite_b2))
                    self.player.projectiles.append(Projectile(self.player.position[0]+60, self.player.position[1]+32, 600.0, -300.0, self.sprite_b2))
                if bullettype == 3:
                    self.player.projectiles.append(Projectile(self.player.position[0]+60, self.player.position[1]+16, 400.0, 0.0, self.sprite_b3))
                if bullettype == 4:
                    self.player.projectiles.append(Projectile(self.player.position[0]+60, self.player.position[1]+32, 400.0, 0.0, self.sprite_b4))

            # update projectiles
            for p in self.player.projectiles:
                p.update(delta)
                # remove projectiles that are off screen
                if (p.x > Config.WIDTH or p.y > Config.HEIGHT or p.y < 0.0):
                    self.player.projectiles.remove(p)

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
                
            # update enemies
            enemies_to_remove = []
            for enemy in self.enemies:
                # Make enemy move to match map scrolling speed
                enemy.x -= Config.SCROLL_SPEED * delta
                should_remove = enemy.update(delta, self.player)
                
                if enemy.x < -50 or should_remove:
                    enemies_to_remove.append(enemy)
            
            for enemy in enemies_to_remove:
                self.enemies.remove(enemy)

            self.ProgressBar.update(delta)
        
            for i in range(len(self.player.pidgeons) - 1):
                self.cd_icon[i].update(delta)
