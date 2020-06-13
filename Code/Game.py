# Game.py

import sys
from Player import *
# importing from enemy file - ARIBA

class Game:
	def __init__(self):
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		self.clock = pygame.time.Clock()
		self.running = True
		self.state =  "start"
		
		# calling load function - FATIMA

		self.cellWidth = WIDTH // 28
		self.cellHeight = HEIGHT // 30

		self.player = Player(self, PLAYER_START_POS)
		# enemies list - ARIBA
		# enemies position list - ARIBA
		# calling make enemies function - ARIBA


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

	# Load(self) - FATIMA
	# Text(..) - FATIMA

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
		# press space bar line - FATIMA
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
		# looping over enemies and - ARIBA
		# updating them - ARIBA

	def PlayingDraw(self):
		self.screen.fill(BLACK) # change for maze - FATIMA
		self.DrawGrid()
		self.player.Draw() 
		# looping over enemies and - ARIBA
		# drawing them - ARIBA
		pygame.display.update()


	# make enemies function - ARIBA