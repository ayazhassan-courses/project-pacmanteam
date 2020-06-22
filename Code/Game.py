# Game.py

import pygame, sys
from Settings import *
from Player import *
from Ghost import * 

class Game:
	def __init__(self):
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		self.clock = pygame.time.Clock()
		self.running = True
		self.state =  "start"

		self.cellWidth = WIDTH // 28
		self.cellHeight = HEIGHT // 31

		self.cellWidthHalf = self.cellWidth // 2
		self.cellHeightHalf = self.cellHeight // 2 

		self.player = Player(self, PLAYER_START_POS)

		self.walls = []
		self.enemies = []
		self.ghostpos = []
		self.Load()
		self.make_enemies()

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

	def Load(self):
		self.background = pygame.image.load('maze2.png')
		self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT)) # To fatima: You don't actually need this line
		
		with open("Maps.txt", 'r') as file:
			for y, line in enumerate(file):
				for x, char in enumerate(line):
					if (char == '1'):
						self.walls.append(vec(x, y))
					elif (char in ['2', '3', '4', '5']):
                        			self.ghostpos.append(vec(x, y))
                    			elif char == 'B':
                        			pygame.draw.rect(self.background, BLACK, (x * self.cellWidth, y * self.cellHeight,
                                                                 self.cellWidth, self.cellHeight))

	def make_enemies(self):
        	for index, pos in enumerate(self.ghostpos):
            		self.enemies.append(Ghost(self, pos, index)) # add the Ghost class as elements into the enemies list
    
	def Text(self, text, screen, color, fonttype, size, pos):
		font = pygame.font.SysFont(fonttype, size)
		introText = font.render(text, False, color)
		screen.blit(introText, pos)

	def DrawGuides(self):
		for x in range (WIDTH // self.cellWidth):
			pygame.draw.line(self.screen, GREY, (x * self.cellWidth, 0), (x * self.cellWidth, HEIGHT))
		for y in range (HEIGHT // self.cellHeight):
			pygame.draw.line(self.screen, GREY, (0, y * self.cellHeight), (WIDTH, y * self.cellHeight)) 

		# for wall in self.walls:
		# 	pygame.draw.rect(self.screen, PURPLE, (int(wall.x * self.cellWidth), int(wall.y * self.cellHeight), self.cellWidth, self.cellHeight))

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
		self.Text('PRESS SPACE BAR TO CONTINUE', self.screen, WHITE, 'arial', 22, ((WIDTH//2-90, HEIGHT//2)))
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
		for ghost in self.enemies:
            		ghost.Update()
		self.player.Update()
		# looping over enemies and - ARIBA
		# updating them - ARIBA

	def PlayingDraw(self):
		self.screen.blit(self.background, (0,0))
		self.DrawGuides()
		self.player.Draw() 
		# looping over enemies and - ARIBA
		# drawing them - ARIBA
		for ghost in self.enemies:
            		ghost.Draw()
		pygame.display.update()
