import pygame, sys

pygame.init()
v = pygame.math.Vector2

w,h= 560, 620
FPS = 60

class Game: 
    def __init__(self):
        self.screen = pygame.display.set_mode((w, h))
        self.game_on = True
        self.state = 'intro'
        self.clock = pygame.time.Clock()
        self.load()

    def load(self):
        self.background = pygame.image.load('maze.jpg')
        self.background = pygame.transform.scale(self.background, (w,h))
    
    def run(self):
        while self.game_on:
            if self.state == 'intro':
                self.start_game()
                self.start_drawing()

            elif self.state == 'playing':
                self.play_game()
                self.play_drawing()
            else:
                self.game_on = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

            
    def start_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_on = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'
    
    def start_drawing(self):
        self.screen.fill((0,0,0))
        self.t('PRESS SPACE BAR TO CONTINUE', self.screen, (255,255,255), 'arial', 22, ((w//2-90, h//2)))
        pygame.display.update()



    def t(self, text, screen, color, fonttype, size, pos):
        f = pygame.font.SysFont(fonttype, size)
        T = f.render(text, False, color)
        screen.blit(T, pos)    

    def play_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_on = False

    def play_drawing(self):
        self.screen.blit(self.background, (0,0))
##        for x in range(w//28):
##            pygame.draw.line((x*))
        pygame.display.update()
        
