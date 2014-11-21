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

        imgdir = "images"
             
        # create the parser
        parser = ConfigParser.ConfigParser()
        parser.read(os.path.join("assets","levels","level" + str(levelnumber) + ".map"))


        # define the foreground & background images
        self.foreground = pygame.image.load(os.path.join(imgdir, parser.get("level", "front"))).convert()
        self.background = pygame.image.load(os.path.join(imgdir, parser.get("level", "back"))).convert()
        self.foregroundx = 0
        self.backgroundx = 0

        # define the duration of the level
        self.duration = parser.get("level", "duration")

        # locate all the obstacles
        self.sections = parser.sections()
        self.obstaclelist = [s for s in self.sections if 'o_' in s]

        # store individual obstacle attributes
        self.obstacle = []
        for item in obstaclelist:
            obstacle.append(parser._sections[item])

        # construct the timeline of events
        self.timeline = parser.items('events')
        self.timekeys = []
        for item in timeline:
            timekeys.append(int(item[0]))

        # pop events as they occur
        timeline = dict(timeline)
        if self.time in self.timekeys:
            timeline.pop(str(self.time))
        
    def render(self):

        screen = pygame.display.get_surface()
        screen.blit(background, (self.backgroundx,0))
        screen.blit(background, (self.backgroundx+self.background.width,0))
        screen.blit(foreground, (self.foregroundx,0))
        screen.blit(background, (self.foregroundx+self.foreground.width,0))

    def update(self):

        self.time += 1

        self.backgroundx -= speed/2
        self.foregroundx -= speed

        if self.backgroundx < -1*(self.background.width):
            if self.backgroundx += self.background.width
        if self.foregroundx < -1*(self.foreground.width):
            if self.foregroundx += self.foreground.width