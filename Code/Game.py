import sys
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

        self.player = None

        self.walls = []

        # new
        self.coins = []
        self.remainingCoins = 0
        # new

        self.ghosts = []
        self.ghostpos = []
        
        self.Load()
        
        self.make_ghosts()

    def Run(self):
        while self.running:
            if (self.state == "start"):
                self.StartEvents()
                # removed function
                self.StartDraw()
            elif (self.state == "playing"):
                self.PlayingEvents()
                self.PlayingUpdate()
                self.PlayingDraw()
            # new
            elif (self.state == "game over"):
                self.GameOverEvents()
                # removed function
                self.GameOverDraw()
            # new
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
                    ## elif (char in ['2', '3', '4', '5']):
                        ## self.ghostpos.append(vec(x, y))
                    elif (char == '2'):
                        self.ghostpos.append(vec(x, y))
                    elif (char == 'B'):
                        pygame.draw.rect(self.background, BLACK, (x * self.cellWidth, y * self.cellHeight,self.cellWidth, self.cellHeight))
                    elif (char == 'P'):
                        self.player = Player(self, vec(x, y))
                    # new 
                    elif (char == 'C'):
                        self.coins.append(vec(x,y))
                        self.remainingCoins += 1
                    # new - map was also changed for this

    def make_ghosts(self):             
        for index, pos in enumerate(self.ghostpos):
            self.ghosts.append(Ghost(self, pos, index))  # add the Ghost class as elements into the ghosts list

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

    # new

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
    # new

    ########################## INTRO FUNCTIONS ###########################

    def StartEvents(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                self.running = False
            if ((event.type == pygame.KEYDOWN) and (pygame.K_SPACE)):
                self.state = "playing"

    # removed function

    def StartDraw(self):
        self.screen.fill(BLACK)
        # new
        self.Text('PRESS SPACE BAR TO CONTINUE', self.screen, WHITE, 'arial', 22, ((WIDTH // 2 - 145, HEIGHT // 2)))
        # new
        pygame.display.update()

    ######################### PLAYING FUNCTIONS ##########################

    def PlayingEvents(self):
        # new
        # if (self.GameOver()): # This function will check for both collision and finished coins
        if (self.remainingCoins <= 0):
            self.state = "game over"
        # new
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
        for ghost in self.ghosts:
            ghost.Update()
        # new
        self.UpdateCoins()
        # new

    def PlayingDraw(self):
        self.screen.blit(self.background, (0,0))
        self.DrawGuides() # remember to comment this out
        # new
        self.DrawCoins()
        # new 
        self.player.Draw() 
        for ghost in self.ghosts:
            ghost.Draw()
        pygame.display.update()


    # new
    ######################### GAME OVER FUNCTIONS ##########################

    def GameOverEvents(self):
        for event in pygame.event.get():
            if ((event.type == pygame.QUIT) or ((event.type == pygame.KEYDOWN) and (pygame.K_SPACE))):
                self.running = False

    # removed function

    def GameOverDraw(self):
        self.screen.fill(BLACK)
        self.Text('GAME OVER', self.screen, RED, 'arial', 22, ((WIDTH // 2 - 55, HEIGHT // 2)))
        pygame.display.update()

    # new