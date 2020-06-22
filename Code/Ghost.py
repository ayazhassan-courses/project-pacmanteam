# Ghost.py
import pygame
from Settings import *
from Game import *

pygame.init()


# vec = pygame.math.Vector2


class Ghost:
    def __init__(self, game, starting_pos, number):
        self.game = game
        self.starting_pos = starting_pos  # grid position
        self.pixel_pos = self.GetPixelPos()
        self.number = number
        self.ghostImg = self.create_Img()
        self.direction = vec(1,0)
        self.personality = self.setPersonality()
        self.state = 'static'

        ##################### variables i dont need but he made them ######
        # self.radius = int(self.app.cellwidth//2.3)

    def Update(self):
        self.state = 'running'
        if self.state == 'running':
            self.pixel_pos += self.direction

    def Draw(self):
        # pygame.draw.circle(self.game.screen,(232, 14, 100), (int(self.pixel_pos.x), int(self.pixel_pos.y)), 16)
        self.game.screen.blit(self.ghostImg, (self.pixel_pos.x, self.pixel_pos.y))
        # self.game.screen.blit(self.ghostImg, (self.starting_pos.x, self.starting_pos.y))

    def GetPixelPos(
            self):  # Returns the position of the Ghost's pixel from the centre of pixel, NOT from the top-left corner of the pixel
        return vec((self.starting_pos.x * self.game.cellWidth),
                   (self.starting_pos.y * self.game.cellHeight))

        # original
        # return vec((self.starting_pos.x * self.game.cellWidth) + self.game.cellWidthHalf,
        #           (self.starting_pos.y * self.game.cellHeight) + self.game.cellHeightHalf)

    def create_Img(self):
        if self.number == 0:
            return pygame.image.load('ghost1.png')
        elif self.number == 1:
            return pygame.image.load('ghost2.png')
        elif self.number == 2:
            return pygame.image.load('ghost3.png')
        elif self.number == 3:
            return pygame.image.load('ghost4.png')

    def setPersonality(self):
        if self.number == 0:
            return "speed"
        elif self.number == 1:
            return "slow"
        elif self.number == 2:
            return "random"
        else:
            return "scared"
