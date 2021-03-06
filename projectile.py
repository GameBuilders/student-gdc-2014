import pygame
import os

class Projectile():

	def __init__(self, x, y, x_vel, y_vel, damage, sprite):
		self.x = x
		self.y = y
		self.x_vel = x_vel
		self.y_vel = y_vel
		self.sprite = sprite
		self.damage = damage

	def update(self,delta):
		self.x += delta * self.x_vel
		self.y += delta * self.y_vel

	def render(self, screen):
		screen.blit(self.sprite, (self.x,self.y))