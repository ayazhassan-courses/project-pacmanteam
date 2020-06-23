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
        #print([int(self.starting_pos.x), int(self.starting_pos.y)])
        x_dir=  path[1][0] - self.starting_pos.x
        y_dir=  path[1][1] - self.starting_pos.y         
        return vec(x_dir, y_dir)
    
    def Djisktra(self,start,target):
        distance_grid = [[math.inf for x in range(28)] for x in range(30)]
        for cell in self.game.walls:
            if cell.x < 28 and cell.y < 30:
                #print([int(cell.y), int(cell.x)])
                distance_grid[int(cell.y)][int(cell.x)] = 9999
       # print(self.game.walls)        
        distance_grid[start[1]][start[0]]=0

        visited=[]
        while True:
            
            value=9997
            
            #find min in distance_grid
            
            for k in range(len(distance_grid)):
                for j in range(len(distance_grid[k])):
                    current_cell_distance=distance_grid[k][j]
                    if [current_cell_distance, j, k] not in visited and current_cell_distance<value:
                        value=current_cell_distance
                        x,y=j,k
            if value==9997:
                break
            else:
                min_value_in_grid=[value, x, y]
            #push min in visited

                visited.append(min_value_in_grid)
                neighbors_4=[0,-1],[0,1],[1,0],[-1,0]
            #check distances to the left, right, up and down of min which are
            # pos and not walls and in grid, if  new value (which is the min_value_in_grid's value +1) is lesser than their
            #current d then update new value in distance_grid
                for b in neighbors_4:
                    x2=min_value_in_grid[1]+b[0]
                    y2=min_value_in_grid[2] +b[1]
                    if (x2) >=0 and (y2) >=0 and (y2) < len(distance_grid) and (x2) < len(distance_grid[0]): #ie positive and in grid
                        if distance_grid[y2][x2] != 9999:        #ie not a wall
                            new_distance_of_neighbor=min_value_in_grid[0]+1 
                            old_distance_of_neighbor=distance_grid[y2][x2]
                            if new_distance_of_neighbor<old_distance_of_neighbor:
                                old_distance_of_neighbor=new_distance_of_neighbor
        print(distance_grid)
        path=[target]
        while target != start:
            next_cell_to_append_in_path=distance_grid[target[1]][target[0]]-1
            #print(next_cell_to_append_in_path)
            for k in range(len(distance_grid)):
                for j in range(len(distance_grid[k])):
                    if distance_grid[k][j]==next_cell_to_append_in_path:
                        break
                if distance_grid[k][j]==next_cell_to_append_in_path:
                    target=[j,k]
                    path.insert(0,target)
                    break
        print(path)
        return path        
