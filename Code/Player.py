# Player.py

import pygame
from Settings import *

pygame.init()
vec = pygame.math.Vector2

class Player:
	def __init__(self, game, startPos):
		self.game = game
		self.gridPos = startPos		
		self.pixPos = self.GetPixPos()
		self.direction = vec(1, 0)
		self.storedDirection = None
		self.radius = self.game.cellWidth // 2 - 2
		self.speed = 1
		self.canMove = True

	def Update(self):

		if (self.canMove):
			self.pixPos += self.direction * self.speed
			self.gridPos.x = self.pixPos.x // self.game.cellWidth 
			self.gridPos.y = self.pixPos.y // self.game.cellHeight 

		if (self.CanTurn()):
			self.direction = self.storedDirection
			self.canMove = self.CanMove()

	def Draw(self):
		pygame.draw.circle(self.game.screen, PLAYER_COLOUR, (int(self.pixPos.x), int(self.pixPos.y)), self.radius)
		pygame.draw.rect(self.game.screen, RED, (int(self.gridPos.x * self.game.cellWidth), int(self.gridPos.y * self.game.cellHeight), self.game.cellWidth, self.game.cellHeight), 1)

	def GetPixPos(self):  # Returns the position of the Player's pixel from the centre, NOT from the top-left corner of the pixel
		return vec(int(self.gridPos.x * self.game.cellWidth) + self.game.cellWidthHalf, int(self.gridPos.y * self.game.cellHeight) + self.game.cellHeightHalf)

	def Move(self, direction):
		self.storedDirection = direction
	
	def CanTurn(self):
		if ((self.storedDirection == vec(0, 1)) or (self.storedDirection == vec(0, -1))):
			return (((self.pixPos.x - self.game.cellWidthHalf) % self.game.cellWidth) == 0)
		elif ((self.storedDirection == vec(1, 0)) or (self.storedDirection == vec(-1, 0))):
			return (((self.pixPos.y - self.game.cellHeightHalf) % self.game.cellHeight) == 0)
		return False

	def CanMove(self):
		return (vec(self.gridPos + self.direction) not in self.game.walls)