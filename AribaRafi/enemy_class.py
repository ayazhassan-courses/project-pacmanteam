import pygame

vec = pygame.math.Vector2



class Enemy(object):
    walkRight = pygame.image.load('ghost.png')
    walkLeft = pygame.image.load('ghost.png')
    def __init__(self, x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walkCount = 0
        self.vel = 3
        self.path = [self.x, self.end]


    def draw(self,screen):
        self.move()
        if self.walkCount + 1 <= 9:
            self.walkCount = 0
        if self.vel > 0:
            screen.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
            walkCount +=1
        else:
            screen.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            walkCount += 1

    def move(self):
        if self.vel > 0:
            if self.x + self.vel< self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel *-1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
