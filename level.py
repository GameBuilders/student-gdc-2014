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

        imgdir = "assets"
             
        # create the parser
        parser = ConfigParser.ConfigParser()
        parser.read(os.path.join("assets","levels","level" + str(levelnumber) + ".map"))


        # define the foreground & background images
        self.foreground = pygame.image.load(os.path.join(imgdir, parser.get("level", "front"))).convert()
        self.background = pygame.image.load(os.path.join(imgdir, parser.get("level", "back"))).convert()
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
        self.timekeys.sort()
        
        self.timeline = dict(self.timeline)
        
    def render(self,screen):

        screen.blit(self.background, (self.backgroundx,0))
        screen.blit(self.background, (self.backgroundx+self.bwidth,0))
        screen.blit(self.foreground, (self.foregroundx,0))
        screen.blit(self.foreground, (self.foregroundx+self.fwidth,0))

    def update(self,delta):

        self.time += delta

        # pop events as they occur
        if not empty(self.timekeys):
            if self.time >= self.timekeys[0]:
                event = self.timeline.pop(str(self.time))
                self.timekeys.pop(0)
                
                # TODO: handle event here
            
        self.backgroundx -= self.speed/2
        self.foregroundx -= self.speed

        if self.backgroundx < -1*(self.bwidth):
             self.backgroundx += self.bwidth
        if self.foregroundx < -1*(self.fwidth):
             self.foregroundx += self.fwidth