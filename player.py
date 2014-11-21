import pygame
from pidgeon import *
from config import *
from sound import *

# Player class. Keeps track of everything we need to know about a player.
class Player():
    # Constructor. Initialize any player variables.
    def __init__(self):
        self.position = [0, Config.HEIGHT/2]
        self.main_pidgeon = Pidgeon(0) # load starting pidgeon
        self.status = 0
        self.pidgeons = [self.main_pidgeon, Pidgeon(1), Pidgeon(2), Pidgeon(3), Pidgeon(4)]
        self.speed = 200
        
        self.found_bird = False
        
        self.projectiles = []
        
        self.lives = 3
        self.dead = False
        self.stun = -1
        self.alpha = 255.0
    
    def get_rect(self):
        return pygame.Rect(self.position[0], self.position[1], 64, 64)
    
    # Kill the player!
    def die(self):
        if not self.dead and (self.stun == -1):
            print "Player died!"
            self.lives -= 1
            play_sound('assets/sounds/pidgeon_dying.wav')
            self.dead = True
    
    # Render the current state of the player.
    def render(self):
        self.main_pidgeon.render(self.position, int(self.alpha))
    
    # Update the state of the player.
    # delta: Time passed (in seconds) since the previous frame.
    def update(self, delta, game_scene):
        if self.found_bird is True:
            game_scene.game.num_pigeons += 1
            game_scene.__init__(game_scene.game)
        
        # death animation
        if self.dead:
            if self.stun == -1:
                self.stun = 3
                pass
            elif self.stun < delta:
                self.dead = False
                self.stun = -1
                self.alpha = 255.0
            else: 
                self.stun -= delta
                if self.alpha > 10:
                    self.alpha -= delta * 255
                else:
                    self.alpha = 255.0

    
        keys_pressed = pygame.key.get_pressed()

        # player movement
        if (keys_pressed[pygame.K_w]):
            self.position[1] = self.position[1] - delta * self.speed
            if (self.position[1] < 0):
                self.position[1] = 0

        if (keys_pressed[pygame.K_s]):
            self.position[1] = self.position[1] + delta * self.speed
            if (self.position[1] + 64 > Config.HEIGHT):
                self.position[1] = Config.HEIGHT - 64

        if (keys_pressed[pygame.K_a]):
            self.position[0] = self.position[0] - delta * self.speed
            if (self.position[0] < 0):
                self.position[0] = 0

        if (keys_pressed[pygame.K_d]):
            self.position[0] = self.position[0] + delta * self.speed
            if (self.position[0] + 64 > Config.WIDTH):
                self.position[0] = Config.WIDTH - 64


        # pidgeon switching
        if (keys_pressed[pygame.K_1]):
            self.main_pidgeon = self.pidgeons[0]
            self.status = 0
            play_sound('assets/sounds/switching.wav')
        elif (keys_pressed[pygame.K_2]):
            if (len(self.pidgeons) >= 2):
                self.main_pidgeon = self.pidgeons[1]
                self.status = 1
                play_sound('assets/sounds/switching.wav')
        elif (keys_pressed[pygame.K_3]):
            if (len(self.pidgeons) >= 3):
                self.main_pidgeon = self.pidgeons[2]
                self.status = 2
                play_sound('assets/sounds/switching.wav')
        elif (keys_pressed[pygame.K_4]):
            if (len(self.pidgeons) >= 4):
                self.main_pidgeon = self.pidgeons[3]
                self.status = 3
                play_sound('assets/sounds/switching.wav')
        elif (keys_pressed[pygame.K_5]):
            if (len(self.pidgeons) >= 5):
                self.main_pidgeon = self.pidgeons[4]
                self.status = 4
                play_sound('assets/sounds/switching.wav')
        
        # Update pidgeon
        self.main_pidgeon.update(delta)
