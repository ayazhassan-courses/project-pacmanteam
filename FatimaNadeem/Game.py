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
		self.Load()
		
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

    def Load(self):
        self.background = pygame.image.load('maze2.png')
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

    def Text(self, text, screen, color, fonttype, size, pos):
        font = pygame.font.SysFont(fonttype, size)
        introText = font.render(text, False, color)
        screen.blit(introText, pos)	

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
		self.player.Update()
		# looping over enemies and - ARIBA
		# updating them - ARIBA

	def PlayingDraw(self):
		self.screen.blit(self.background, (0,0) # change for maze - FATIMA
		self.DrawGrid()
		self.player.Draw() 
		# looping over enemies and - ARIBA
		# drawing them - ARIBA
		pygame.display.update()


	# make enemies function - ARIBA
