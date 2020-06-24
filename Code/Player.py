# Player.py

import pygame #[2]
from Settings import * 

pygame.init()

class Player:
	def __init__(self, game, startPos):
		self.game = game
		self.gridPos = startPos		
		self.pixPos = self.GetPixPos()
		self.direction = vec(1, 0)
		self.storedDirection = self.direction
		self.radius = self.game.cellWidth // 2 - 2
		self.speed = 2
		self.canMove = True

	def Update(self):

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
			
		## Basic logic of updating according to movability of Pacman, checking pixel position of Pacman from its topleftcorner
		## and turning it accordingly in the right direction adapted by [2]

	def Draw(self):
		pygame.draw.circle(self.game.screen, PLAYER_COLOUR, (int(self.pixPos.x), int(self.pixPos.y)), self.radius)
		pygame.draw.rect(self.game.screen, RED, (int(self.gridPos.x * self.game.cellWidth), int(self.gridPos.y * self.game.cellHeight), self.game.cellWidth, self.game.cellHeight), 1)
		
		## [2]
		
	def GetPixPos(self):  # Returns the position of the Player's pixel from the centre, NOT from the top-left corner of the pixel
		return vec(int(self.gridPos.x * self.game.cellWidth) + self.game.cellWidthHalf, int(self.gridPos.y * self.game.cellHeight) + self.game.cellHeightHalf)
		
		## Basic logic of drawing Pacman and adjusting to pixPos adapted by [2]
		
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
	
		## Basic logic of checking turnability and avoiding walls by [2]
