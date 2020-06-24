# Game.py

import sys # [3]
from Player import * 
from Ghost import * 

class Game: # Basic logic of making Game class is adapted from [1]

    def __init__(self): # Basic logic of making __Init__(self) is adapted from [1]
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state =  "start"

        self.cellWidth = WIDTH // 28
        self.cellHeight = HEIGHT // 31

        self.cellWidthHalf = self.cellWidth // 2
        self.cellHeightHalf = self.cellHeight // 2 

        self.player = None

        self.walls = []

        self.coins = []
        self.remainingCoins = 0

        self.ghosts = []
        
        self.Load()

    def Run(self): # Basic logic of making Run(self) is adapted from [1]
        while self.running:
            if (self.state == "start"):
                self.StartEvents()
                self.StartDraw()
            elif (self.state == "playing"):
                self.PlayingEvents()
                self.PlayingUpdate()
                self.PlayingDraw()
            elif (self.state == "game over"):
                self.GameOverEvents()
                self.GameOverDraw()
            else:
                self.running = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
       
    ######################### HELPER FUNCTIONS ###########################

    def Load(self): # Basic logic of making Load(self) is adapted from [1]
        self.background = pygame.image.load('maze2.png')
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT)) # To fatima: You don't actually need this line

        with open("Maps.txt", 'r') as file:
            for y, line in enumerate(file):
                for x, char in enumerate(line):
                    if (char == '1'):
                        self.walls.append(vec(x, y))
                    elif (char in "2"):
                        self.ghosts.append(Ghost(self, vec(x, y), char))
                    elif (char == 'B'):
                        pygame.draw.rect(self.background, BLACK, (x * self.cellWidth, y * self.cellHeight,self.cellWidth, self.cellHeight))
                    elif (char == 'P'):
                        self.player = Player(self, vec(x, y))
                    elif (char == 'C'):
                        self.coins.append(vec(x,y))
                        self.remainingCoins += 1

    def Text(self, text, screen, color, fonttype, size, pos): # [1]
        font = pygame.font.SysFont(fonttype, size)
        introText = font.render(text, False, color)
        screen.blit(introText, pos)
    
#    def DrawGuides(self): # [1]
#        for x in range (WIDTH // self.cellWidth):
#            pygame.draw.line(self.screen, GREY, (x * self.cellWidth, 0), (x * self.cellWidth, HEIGHT))
#        for y in range (HEIGHT // self.cellHeight):
#            pygame.draw.line(self.screen, GREY, (0, y * self.cellHeight), (WIDTH, y * self.cellHeight)) 

    def GameOver(self):
        if (self.remainingCoins <= 0):
            return True

        for ghost in self.ghosts:
            if (ghost.foundPlayer):
                return True

        return False

    ########################## COIN FUNCTIONS ###########################

    def UpdateCoins(self):
        coinInd = 0
        while (coinInd < self.remainingCoins):
            if (self.coins[coinInd] == self.player.gridPos):
                self.coins.pop(coinInd)
                self.remainingCoins -= 1
                break   
            coinInd += 1

    def DrawCoins(self):
        for coinPos in self.coins:
            pygame.draw.circle(self.screen, COIN_COLOUR, (int(coinPos.x * self.cellWidth) + self.cellWidthHalf, int(coinPos.y * self.cellHeight) + self.cellHeightHalf), 5)

    ########################## INTRO FUNCTIONS ###########################

    def StartEvents(self): # [1]
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                self.running = False
            if ((event.type == pygame.KEYDOWN) and (pygame.K_SPACE)):
                self.state = "playing"

    def StartDraw(self): # [1]
        self.screen.fill(BLACK)
        self.Text('PRESS SPACE BAR TO CONTINUE', self.screen, WHITE, 'arial', 22, ((WIDTH // 2 - 145, HEIGHT // 2)))
        pygame.display.update()
        
    ######################### PLAYING FUNCTIONS ##########################

    def PlayingEvents(self): # Basic logic of making PlayingEvents(self) is adapted from [1]
        if (self.GameOver()):
            self.state = "game over"

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

    def PlayingUpdate(self): # [1]
        self.player.Update()
        for ghost in self.ghosts:
            ghost.Update()

        self.UpdateCoins()
        
    def PlayingDraw(self): # [1]
        self.screen.blit(self.background, (0,0))
        # self.DrawGuides() 
        self.DrawCoins()
        self.player.Draw() 
        for ghost in self.ghosts:
            ghost.Draw()
        pygame.display.update()

    ######################### GAME OVER FUNCTIONS ##########################

    def GameOverEvents(self):
        for event in pygame.event.get():
            if ((event.type == pygame.QUIT) or ((event.type == pygame.KEYDOWN) and (pygame.K_SPACE))):
                self.running = False

    def GameOverDraw(self):
        self.screen.fill(BLACK)
        self.Text('GAME OVER', self.screen, RED, 'arial', 22, ((WIDTH // 2 - 55, HEIGHT // 2)))
        pygame.display.update()
