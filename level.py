import ConfigParser
import pygame
import pygame.locals
import json
import os
import config

class Level(object):
    def __init__(self, levelnumber):

        # counter
        self.time = 0
        self.speed = 2

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
        self.duration = parser.get("level", "duration")

        # locate all the obstacles
        self.sections = parser.sections()
        self.obstaclelist = [s for s in self.sections if 'o_' in s]

        # store individual obstacle attributes
        self.obstacle = []
        for item in self.obstaclelist:
            self.obstacle.append(parser._sections[item])

        # construct the timeline of events
        self.timeline = parser.items('events')
        self.timekeys = []
        for item in self.timeline:
            self.timekeys.append(int(item[0]))

        # pop events as they occur
        self.timeline = dict(self.timeline)
        if self.time in self.timekeys:
            self.timeline.pop(str(self.time))
        
    def render(self,screen):

        screen.blit(self.background, (self.backgroundx,0))
        screen.blit(self.background, (self.backgroundx+self.bwidth,0))
        screen.blit(self.foreground, (self.foregroundx,0))
        screen.blit(self.foreground, (self.foregroundx+self.fwidth,0))
        pass

    def update(self,delta):

        self.time += delta

        self.backgroundx -= self.speed/2
        self.foregroundx -= self.speed

        if self.backgroundx < -1*(self.bwidth):
             self.backgroundx += self.bwidth
        if self.foregroundx < -1*(self.fwidth):
             self.foregroundx += self.fwidth