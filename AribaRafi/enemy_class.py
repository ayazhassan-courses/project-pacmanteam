import pygame
from player_class import *

vec = pygame.math.Vector2



class Enemy:
    def __init__(self, app):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.draw = draw(self)

    def get_pix_pos(self):
        return vec((self.gridPos.x * self.app.cellWidth) + (self.app.cellWidth // 2),(self.gridPos.y * self.app.cellHeight) + (self.app.cellHeight // 2))

    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(self.app.screen, (255,255,255), int(self.pix_pos.x), int(self.pix_pos.y)), 15)


    # walkRight = pygame.image.load('ghost.png')
    # walkLeft = pygame.image.load('ghost.png')
    # def __init__(self, x,y,width,height,end):
    #     self.x = x
    #     self.y = y
    #     self.width = width
    #     self.height = height
    #     self.end = end
    #     self.walkCount = 0
    #     self.vel = 3
    #     self.path = [self.x, self.end]
    #
    # #
    # def draw(self,screen):
        #self.move()
        # if self.walkCount + 1 <= 9:
        #     self.walkCount = 0
        # if self.vel > 0:
        #     screen.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
        #     walkCount +=1
        # else:
        #     screen.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
        #     walkCount += 1

    # def move(self):
    #     if self.vel > 0:
    #         if self.x + self.vel< self.path[1]:
    #             self.x += self.vel
    #         else:
    #             self.vel = self.vel *-1
    #             self.walkCount = 0
    #     else:
    #         if self.x - self.vel > self.path[0]:
    #             self.x += self.vel
    #         else:
    #             self.vel = self.vel * -1
    #             self.walkCount = 0
