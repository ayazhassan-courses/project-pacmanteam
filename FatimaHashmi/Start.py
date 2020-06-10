import pygame, sys
from settings import *

pygame.init()
v = pygame.math.Vector2

class Game: 
    def __init__(self):
        self.screen = pygame.display.set_mode((w, h))
        self.game_on = True
        self.state = 'intro'
        self.clock = pygame.time.Clock()
        self.load()
        self.cell_width = w//28
        self.cell_height = h//30

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



#############helper_functions############################

    def load(self):
        self.background = pygame.image.load('maze2.png')
        self.background = pygame.transform.scale(self.background, (w,h))

    def t(self, text, screen, color, fonttype, size, pos):
        f = pygame.font.SysFont(fonttype, size)
        T = f.render(text, False, color)
        screen.blit(T, pos)

    def grid(self):
        for i in range(w//(self.cell_width)):
            pygame.draw.line(self.screen,GREY, ((i*self.cell_width),0),((i*self.cell_width),h))
        for i in range(h//(self.cell_height)):
            pygame.draw.line(self.screen,GREY, (0,(i*self.cell_height)),(w,(i*self.cell_height)))   
            
            
#############start_functions############################
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

#############playing_functions############################
    def play_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_on = False

    def play_drawing(self):
        self.screen.blit(self.background, (0,0))
        self.grid()
        pygame.display.update()
        
