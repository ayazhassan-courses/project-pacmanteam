# Player.py

import pygame # [2]
from Settings import * 

pygame.init()

class Player: # Basic logic of making Player class is adapted from [1]
	def __init__(self, game, startPos):
		self.game = game
		self.gridPos = startPos		
		self.pixPos = self.GetPixPos()
		self.direction = vec(1, 0)
		self.storedDirection = self.direction
		self.radius = self.game.cellWidth // 2 - 2
		self.speed = 2
		self.canMove = True

	def Update(self): # Basic logic of making Update(self) is adapted from [1]
		if (self.canMove):
			self.pixPos += self.direction * self.speed 

			topLeftCorner = vec(self.pixPos.x - self.game.cellWidthHalf, self.pixPos.y - self.game.cellHeightHalf)
			if ((topLeftCorner.x % self.game.cellWidth) == 0):
				self.gridPos.x = topLeftCorner.x // self.game.cellWidth 
			if ((topLeftCorner.y % self.game.cellHeight) == 0):
				self.gridPos.y = topLeftCorner.y // self.game.cellHeight
			
		if (self.CanTurn()):
			self.direction = self.storedDirection
			self.canMove = self.CanMove() 

	def Draw(self): # [1]
		pygame.draw.circle(self.game.screen, PLAYER_COLOUR, (int(self.pixPos.x), int(self.pixPos.y)), self.radius)
		pygame.draw.rect(self.game.screen, RED, (int(self.gridPos.x * self.game.cellWidth), int(self.gridPos.y * self.game.cellHeight), self.game.cellWidth, self.game.cellHeight), 1)
		
	def GetPixPos(self): # [1]
		return vec(int(self.gridPos.x * self.game.cellWidth) + self.game.cellWidthHalf, int(self.gridPos.y * self.game.cellHeight) + self.game.cellHeightHalf)
		
	def Move(self, direction): # [1]
		self.storedDirection = direction
		
	def CanTurn(self): # [1]
		if ((self.storedDirection == vec(0, 1)) or (self.storedDirection == vec(0, -1))):
			return (((self.pixPos.x - self.game.cellWidthHalf) % self.game.cellWidth) == 0)
		elif ((self.storedDirection == vec(1, 0)) or (self.storedDirection == vec(-1, 0))):
			return (((self.pixPos.y - self.game.cellHeightHalf) % self.game.cellHeight) == 0)
		return False
		
		
	def CanMove(self): # [1]
		return (vec(self.gridPos + self.direction) not in self.game.walls)