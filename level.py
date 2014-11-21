import ConfigParser
import pygame
import pygame.locals
import json
import os
import config
from entity import *
from enemy import *
from spritesheet import *

class Level(object):
    def __init__(self, levelnumber):

        self.spritesheet = Spritesheet(os.path.join('assets', 'pidgeon_anim.png'), 64, 64)
        self.bullet_sprite = pygame.image.load(os.path.join(os.path.join('assets','projectiles'),'gray.png'))

    
        # counter
        self.time = 0
        self.speed = Config.SCROLL_SPEED

        directory = os.path.join("assets","levels")
             
        # create the parser
        parser = ConfigParser.ConfigParser()
        parser.read(os.path.join(directory,"level" + str(levelnumber) + ".map"))


        # define the foreground & background images
        self.foreground = pygame.image.load(os.path.join(directory, parser.get("level", "front"))).convert_alpha()
        self.background = pygame.image.load(os.path.join(directory, parser.get("level", "back"))).convert_alpha()
        self.foreground.set_colorkey( pygame.Color('red') )
        self.foregroundx = 0
        self.backgroundx = 0
        self.fwidth = self.foreground.get_width()
        self.bwidth = self.background.get_width()

        # define the duration of the level
        self.duration = int(parser.get("level", "duration"))

        # locate all the obstacles
        self.sections = parser.sections()
        self.obstaclelist = [s for s in self.sections if 'o_' in s]

        # store individual obstacle attributes
        self.obstacle = dict()
        for item in self.obstaclelist:
            self.obstacle[item] = parser._sections[item]
            self.obstacle[item]['sprite'] = pygame.image.load(self.obstacle[item]['img'])

        # construct the timeline of events
        self.timeline = parser.items('events')
        self.timekeys = []
        for item in self.timeline:
            self.timekeys.append(int(item[0]))
        
        self.timekeys, self.timeline = zip(*sorted(zip(self.timekeys, self.timeline)))    
        self.timekeys = list(self.timekeys)
        self.timeline = dict(self.timeline)
        
    def render(self,screen):

        screen.blit(self.background, (self.backgroundx,0))
        screen.blit(self.background, (self.backgroundx+self.bwidth,0))
        screen.blit(self.foreground, (self.foregroundx,0))
        screen.blit(self.foreground, (self.foregroundx+self.fwidth,0))
        pass

    def update(self,delta, game_scene):

        self.time += delta
        
        # pop events as they occur
        if self.timekeys:
            if self.time >= self.timekeys[0]:
                event = self.timeline.pop( str(self.timekeys[0]) )
                
                event_list = event.split(",")
                self.timekeys.pop(0)
                
                obstacle = self.obstacle[event_list[0]]
                
                if obstacle['type'] == '1':
                    # Enemy
                    enemy = Enemy(self.spritesheet, int(event_list[1]), self.bullet_sprite)
                    game_scene.enemies.append(enemy)
                else:
                    # Obstacles
                    obs = Entity(obstacle['sprite'], Config.WIDTH + 32, int(event_list[1]), int(obstacle['type']))
                    game_scene.obstacles.append(obs)
                
                # event[0] contains the object name
                # event[1] contains the y-coordinate at which it should be placed
                # TODO: handle event here

        if self.time < self.duration:

            self.backgroundx -= self.speed * delta /2
            self.foregroundx -= self.speed * delta

            if self.backgroundx < -1*(self.bwidth):
                 self.backgroundx += self.bwidth
            if self.foregroundx < -1*(self.fwidth):
                 self.foregroundx += self.fwidth
