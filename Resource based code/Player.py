# Player.py

import pygame
from Settings import *

pygame.init()
vec = pygame.math.Vector2

class Player:
	def __init__(self, game, pos):
		self.game = game
		self.gridPos = pos		
		self.pixPos = self.GetPixPos()
		self.direction = vec(1, 0)

	def Update(self):
		self.pixPos += self.direction
		self.gridPos.x = ((self.pixPos.x - (self.game.cellWidth // 2)) // self.game.cellWidth) 
		self.gridPos.y = ((self.pixPos.y - (self.game.cellHeight // 2)) // self.game.cellHeight) 

	def Draw(self):
		pygame.draw.circle(self.game.screen, PLAYER_COLOUR, (int(self.pixPos.x), int(self.pixPos.y)), self.game.cellWidth // 2 - 2)
		pygame.draw.rect(self.game.screen, RED, (self.gridPos.x * self.game.cellWidth, self.gridPos.y * self.game.cellHeight, self.game.cellWidth, self.game.cellHeight), 1)

	def Move(self, direction):
		self.direction = direction

	def GetPixPos(self):
		return vec((self.gridPos.x * self.game.cellWidth) + (self.game.cellWidth // 2), (self.gridPos.y * self.game.cellHeight) + (self.game.cellHeight // 2))
		print(self.gridPos, self.pixPos)