# player_class.py

import pygame
from settings import *

pygame.init()
vec = pygame.math.Vector2

class Player:
	def __init__(self, app, pos):
		self.app = app
		self.gridPos = pos		
		self.pixPos = self.GetPixPos()
		self.direction = vec(1, 0)

	def Update(self):
		self.pixPos += self.direction
		self.gridPos.x = ((self.pixPos.x - (self.app.cellWidth // 2)) // self.app.cellWidth) 
		self.gridPos.y = ((self.pixPos.y - (self.app.cellHeight // 2)) // self.app.cellHeight) 

	def Draw(self):
		pygame.draw.circle(self.app.screen, PLAYER_COLOUR, (int(self.pixPos.x), int(self.pixPos.y)), self.app.cellWidth // 2 - 2)
		pygame.draw.rect(self.app.screen, RED, (self.gridPos.x * self.app.cellWidth, self.gridPos.y * self.app.cellHeight, self.app.cellWidth, self.app.cellHeight), 1)

	def Move(self, direction):
		self.direction = direction

	def GetPixPos(self):
		return vec((self.gridPos.x * self.app.cellWidth) + (self.app.cellWidth // 2), (self.gridPos.y * self.app.cellHeight) + (self.app.cellHeight // 2))
		print(self.gridPos, self.pixPos)