# Ghost.py
import pygame, math
from Settings import *
from Game import *
pygame.init()
vec = pygame.math.Vector2

class Ghost:
    def __init__(self, game, starting_pos, number):
        self.game = game
        self.starting_pos = starting_pos  # grid position
        self.pixel_pos = self.GetPixelPos()
        self.number = number
        self.ghostImg = self.create_Img()
        self.direction = vec(0,1)
 #      self.personality = self.setPersonality()
        self.state = 'static'
        self.target = None

    def Update(self):
        self.state = 'running'
        if self.state == 'running':
                
            self.target = self.set_target()
            
            if self.target != self.starting_pos:
                self.pixel_pos += self.direction
                #print(self.starting_pos)
                if self.time_to_move():
                    self.direction =self.move(self.target)
        # Setting grid position in reference to pix position
        self.starting_pos[0] = (self.pixel_pos[0] +
                            self.game.cellWidth//2)//self.game.cellWidth+1
        self.starting_pos[1] = (self.pixel_pos[1] +
                            self.game.cellHeight//2)//self.game.cellHeight+1
             
        
    def Draw(self):
        # pygame.draw.circle(self.game.screen,(232, 14, 100), (int(self.pixel_pos.x), int(self.pixel_pos.y)), 16)
        self.game.screen.blit(self.ghostImg, (self.pixel_pos.x, self.pixel_pos.y))
        # self.game.screen.blit(self.ghostImg, (self.starting_pos.x, self.starting_pos.y))

    def GetPixelPos(
            self):  # Returns the position of the Ghost's pixel from the centre of pixel, NOT from the top-left corner of the pixel
        return vec((self.starting_pos.x * self.game.cellWidth),
                   (self.starting_pos.y * self.game.cellHeight))

    def create_Img(self):
        
#        if self.number == 0:
        return pygame.image.load('ghost1.png')
##        elif self.number == 1:
##            return pygame.image.load('ghost2.png')
##        elif self.number == 2:
##            return pygame.image.load('ghost3.png')
##        elif self.number == 3:
##            return pygame.image.load('ghost4.png')

##    def setPersonality(self):
##        if self.number == 0:
##            return "speed"
##        elif self.number == 1:
##            return "slow"
##        elif self.number == 2:
##            return "random"
##        else:
##            return "scared"
        
    def set_target(self):
##        if self.game.player.gridPos[0] > 28//2 and self.game.player.gridPos[1] > 31//2:
##            return vec(1, 1)
##        if self.game.player.gridPos[0] > 28//2 and self.game.player.gridPos[1] < 31//2:
##            return vec(1, 31-2)
##        if self.game.player.gridPos[0] < 28//2 and self.game.player.gridPos[1] > 31//2:
##            return vec(28-2, 1)
##        else:
##            return vec(28-2, 31-2)
        return self.game.player.gridPos
        
    def time_to_move(self):
        if int(self.pixel_pos.x) % self.game.cellWidth == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                return True
        if int(self.pixel_pos.y) % self.game.cellHeight == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                return True
        return False
    
    def move(self, target):
        path = self.Djisktra([int(self.starting_pos.x), int(self.starting_pos.y)],[int(target[0]),int(target[1])])
        p_x=  path[1][0] - self.starting_pos.x
        p_y=  path[1][1] - self.starting_pos.y 
        #print(vec(p_x, p_y))
        return vec(p_x, p_y)

    def Djisktra(self,s,t):
    ##    grid = [[0 for x in range(28)] for x in range(30)]
    ##        for cell in self.game.walls:
    ##            if cell.x < 28 and cell.y < 30:
    ##                grid[int(cell.y)][int(cell.x)] = 1

        dg = [[math.inf for x in range(28)] for x in range(30)]
        for cell in self.game.walls:
            if cell.x < 28 and cell.y < 30:
                dg[int(cell.y)][int(cell.x)] = 9999

        dg[s[1]][s[0]]=0

        v=[]

        while True:

            i=9997
            #x,y=0,0
            for k in range(len(dg)):
                for j in range(len(dg[k])):
                    if [dg[k][j],j,k] not in v and dg[k][j]<i:
                        i=dg[k][j]
                        x,y=j,k
            if i==9997:
                break
            else:
                a=[i,x,y]
            #find min in dg
            #remove min from q and push min in visited
                v.append(a)
                b1=[0,-1],[0,1],[1,0],[-1,0]
                #check distances to the left, right, up and down of min which are
            # pos and not walls and in grid, if  min's d +1 is lesser than their
            #current d then update value in dg
                for b in b1:
                    ##a=[0,2,3]        b=[0,1]
                    x2=a[1]+b[0]
                    y2=a[2] +b[1]
                    if (a[1]+b[0]) >=0 and (a[2] +b[1]) >=0 and (a[2] +b[1]) < len(dg) and (a[1] +b[0]) < len(dg[0]):
                        if dg[y2][x2] != 9999:
                            if (a[0]+1)<dg[y2][x2]:
                                dg[y2][x2]=a[0]+1
                            #    print(dg)



        path=[t]

        while t != s:
           # print(dg[t[1]][t[0]])
            p=dg[t[1]][t[0]]-1
            for k in range(len(dg)):
                for j in range(len(dg[k])):
                    if dg[k][j]==p:
                        break
                if dg[k][j]==p:
                    t=[j,k]
                    path.insert(0,t)

                    break

        return path        
