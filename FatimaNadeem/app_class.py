# app_class.py

import sys
from player_class import *

class App:
	def __init__(self):
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		self.clock = pygame.time.Clock()
		self.running = True
		self.state =  "start"
		
		self.cellWidth = WIDTH // 28
		self.cellHeight = HEIGHT // 30

		self.player = Player(self, PLAYER_START_POS)

	def Run(self):
		while self.running:
			if (self.state == "start"):
				self.StartEvents()
				self.StartUpdate()
				self.StartDraw()
			elif (self.state == "playing"):
				self.PlayingEvents()
				self.PlayingUpdate()
				self.PlayingDraw()
			else:
				self.running = False
			self.clock.tick(FPS)
		pygame.quit()
		sys.exit()

	######################### HELPER FUNCTIONS ###########################

	def DrawGrid(self):
		for x in range (WIDTH // self.cellWidth):
			pygame.draw.line(self.screen, GREY, (x * self.cellWidth, 0), (x * self.cellWidth, HEIGHT))
		for y in range (HEIGHT // self.cellHeight):
			pygame.draw.line(self.screen, GREY, (0, y * self.cellHeight), (WIDTH, y * self.cellHeight)) 



	########################## INTRO FUNCTIONS ###########################

	def StartEvents(self):
		for event in pygame.event.get():
			if (event.type == pygame.QUIT):
				self.running = False
			if ((event.type == pygame.KEYDOWN) and (pygame.K_SPACE)):
				self.state = "playing"

	def StartUpdate(self):
		pass
	def StartDraw(self):
		self.screen.fill(BLACK)
		pygame.display.update()

	######################### PLAYING FUNCTIONS ##########################

	def PlayingEvents(self):
		for event in pygame.event.get():
			if (event.type == pygame.QUIT):
				self.running = False
			if (event.type == pygame.KEYDOWN):
				if (event.key == pygame.K_LEFT):
					self.player.Move(vec(-1, 0))
				if (event.key == pygame.K_RIGHT):
					self.player.Move(vec(1, 0))
				if (event.key == pygame.K_UP):
					self.player.Move(vec(0, -1))
				if (event.key == pygame.K_DOWN):
					self.player.Move(vec(0, 1))

	def PlayingUpdate(self):
		self.player.Update()

	def PlayingDraw(self):
		self.screen.fill(BLACK)
		self.DrawGrid()
		self.player.Draw() 
		pygame.display.update()