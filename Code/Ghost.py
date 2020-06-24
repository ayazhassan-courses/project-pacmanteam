# Ghost.py

import pygame, math
from Settings import *

pygame.init()

class Ghost:
    def __init__(self, game, currentPos, number):
        self.game = game
        self.currentPos = currentPos  # grid position
        self.pixPos = self.GetPixelPos()
        # self.number = number
        self.ghostImg = self.CreateImg()
        self.direction = vec(0,-1) 
        self.G = self.LoadGraph()
        self.state = 'static'
        self.target = None
        self.foundPlayer = False
        self.speed = 2

    def Update(self):       
        self.target = self.GetTarget()
        
        if (self.target != self.currentPos):
            self.Move()
            self.pixPos += self.direction * self.speed
        else:
            self.foundPlayer = True

        self.currentPos.x = self.pixPos.x // self.game.cellWidth 
        self.currentPos.y = self.pixPos.y // self.game.cellHeight 
             
        
    def Draw(self):
        self.game.screen.blit(self.ghostImg, (self.pixPos.x, self.pixPos.y))

    def GetPixelPos(self):  # Returns the position of the Ghost's pixel from the top-left corner of the pixel
        return vec(int(self.currentPos.x * self.game.cellWidth),
                   int(self.currentPos.y * self.game.cellHeight))

    def CreateImg(self):
        
#        if self.number == 0:
        return pygame.image.load('ghost1.png')
##        elif self.number == 1:
##            return pygame.image.load('ghost2.png')
##        elif self.number == 2:
##            return pygame.image.load('ghost3.png')
##        elif self.number == 3:
##            return pygame.image.load('ghost4.png')
        
    def GetTarget(self):
        return self.game.player.gridPos

    # Graph helper functions

    def LoadGraph(self):
        G = {}

        for y in range(31):
            for x in range(28):
                node = (x, y)
                G[node] = []

                if ((x > 0) and (vec(x - 1, y) not in self.game.walls)):
                    G[node].append(((x - 1, y), 1))

                if ((x < 27) and (vec(x + 1, y) not in self.game.walls)):
                    G[node].append(((x + 1, y), 1))

                if ((y > 0) and (vec(x, y - 1) not in self.game.walls)):
                    G[node].append(((x, y - 1), 1))

                if ((y < 30) and (vec(x, y + 1) not in self.game.walls)):
                    G[node].append(((x, y + 1), 1))

        return G


    # Priority Queue helper functions

    def IsEmpty(self, Q):
        return (len(Q) == 0)

    def Enqueue(self, Q, item):
        Q.append(item)

    def DMinDequeue(self, Q, dist):
        lenq = len(Q)
        minDist = float("inf")
        minInd = 0

        for i in range(lenq):
            if (dist[Q[i]][1] < minDist):
                minDist = dist[Q[i]][1]
                minInd = i

        return Q.pop(minInd)


    def Dijkstra(self, sv, ev):
        unvisitedQ = [sv]
        visited = []
        dist = {sv: [sv, 0]}

        for node in self.G:
            if (node != sv):
                    dist[node] = [None, float("inf")]
                    self.Enqueue(unvisitedQ, node)

        while (not self.IsEmpty(unvisitedQ)):
            current = self.DMinDequeue(unvisitedQ, dist)

            for node2 in self.G[current]:
                if (node2 not in visited):
                    alt = dist[current][1] + node2[1]

                    if (alt < dist[node2[0]][1]):  
                        dist[node2[0]] = [current, alt]

            visited.append(current)

        child = ev
        retLst = []

        while (child != sv):
            retLst.insert(0, child)
            child = dist[child][0]
            
        return retLst

    def CanTurn(self, direction):
        if ((direction == vec(0, 1)) or (direction == vec(0, -1))):
            return ((self.pixPos.x % self.game.cellWidth) == 0)
        elif ((direction == vec(1, 0)) or (direction == vec(-1, 0))):
            return ((self.pixPos.y % self.game.cellHeight) == 0)
        return False

    def Move(self):
        sc = (self.currentPos.x, self.currentPos.y)
        ec = (self.target.x, self.target.y)
        path = self.Dijkstra(sc, ec)
        
        direction = vec(path[0][0] - self.currentPos.x, path[0][1] - self.currentPos.y)

        if (self.CanTurn(direction)):
            self.direction = direction
