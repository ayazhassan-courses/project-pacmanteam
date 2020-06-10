import pygame, sys
from settings import *
from enemy_class import *
pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'


    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()

            else:
                self.running = False
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

####################################################### helper FUNCTIONS ####
    def draw_text(self, words, screen, pos, size, colour, font_name):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        pos[0] = pos[0] - text_size[0]//2
        pos[1] = pos[1] - text_size[1] // 2
        screen.blit(text, pos)


####################################################### INTRO FUNCTION S#####

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'

    def start_update(self):
        pass

    def start_draw(self):
        self.screen.fill(BLACK)
        self.draw_text("PUSH SPACE BAR",self.screen,[width//2,height//2],START_TEXT_SIZE, (170,132,58), START_FONT)
        self.draw_text("ONE PLAYER ONLY", self.screen, [width // 2, height // 2+50], START_TEXT_SIZE, (33, 137, 156),
                       START_FONT)

        pygame.display.update()


####################################################### PLAYING FUNCTION S#####

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def playing_update(self):
        pass

    def playing_draw(self):
        self.screen.fill(RED)
        pygame.display.update()

        goblin = Enemy(100, 410, 64, 64, 450)

        pygame.display.update()


