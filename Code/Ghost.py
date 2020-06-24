# Ghost.py

import pygame, math # [2],[4]
from Settings import *

pygame.init()

class Ghost: # Basic logic of making Ghost class is adapted from [1]
    def __init__(self, game, currentPos, id):
        self.game = game
        self.currentPos = currentPos  # grid position
        self.pixPos = self.GetPixelPos()
        # self.id = id
        # id = '2' => blue ghost
        # id = '3' => red ghost
        self.ghostImg = self.CreateImg()
        self.direction = vec(0,-1) 
        self.G = self.LoadGraph()
        self.state = 'static'
        self.target = self.GetTarget()
        self.foundPlayer = False
        self.speed = 2
        
    def Update(self): # Basic logic of making Update(self) is adapted from [1]       
        self.target = self.GetTarget()
        
        if (self.target != self.currentPos):
            self.Move()
            self.pixPos += self.direction * self.speed
        else:
            self.foundPlayer = True

        self.currentPos.x = self.pixPos.x // self.game.cellWidth 
        self.currentPos.y = self.pixPos.y // self.game.cellHeight 
        
    def Draw(self): # [1]
        self.game.screen.blit(self.ghostImg, (self.pixPos.x, self.pixPos.y))

    def GetPixelPos(self): # [1]
        return vec(int(self.currentPos.x * self.game.cellWidth),
                   int(self.currentPos.y * self.game.cellHeight))

    def CreateImg(self): # Basic logic of making CreateImg(self) is adapted from [1]   
        # if self.id == '2':
        return pygame.image.load('ghost1.png')
        # elif self.id == '3':
        #     return pygame.image.load('ghost2.png')
        
    def GetTarget(self): # [1]
        return self.game.player.gridPos
    
    # Graph helper functions

    def LoadGraph(self):
        G = {}

        for y in range(31):
            for x in range(28):
                if (vec(x, y) not in self.game.walls):
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

    # def Algorithm(self, sv, ev):
    #     if (self.id == '2'):
    #         return self.Dijkstra(sv, ev)
    #     else:
    #         path = self.DFS(sv, ev)
    #         path.pop(0)
    #         return path

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

    # Dijkstra

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

    # Stack helper functions

    # IsEmpty is already here

    # def Top(self, S):
    #     if (len(S) != 0):
    #         return S[-1]

    # def Pop(self, S):
    #     if (len(S) != 0):
    #         return S.pop()

    # def Push(self, S, item):
    #     S.append(item)

    # # DFS
    
    # def DFS(self, sv, ev):
    #     stack = [sv]
    #     visited = []

    #     while ((not self.IsEmpty(stack)) and (self.Top(stack) != ev)):
    #         neighbours = self.G[self.Top(stack)]
    #         i = 0
    #         neighboursLen = len(neighbours)
    #         while i <= neighboursLen:
    #             if ((i < neighboursLen) and (neighbours[i][0] not in visited)):
    #                 self.Push(stack, neighbours[i][0])
    #                 visited.append(neighbours[i][0])
    #                 break
    #             elif (i == neighboursLen):
    #                 self.Pop(stack)
    #             i += 1

    #     return stack
    
    def CanTurn(self, direction): # Basic logic of making CanTurn(self, direction) is adapted from [1] 
        if ((direction == vec(0, 1)) or (direction == vec(0, -1))):
            return ((self.pixPos.x % self.game.cellWidth) == 0)
        elif ((direction == vec(1, 0)) or (direction == vec(-1, 0))):
            return ((self.pixPos.y % self.game.cellHeight) == 0)
        return False
    
        ## Basic logic of checking condition of movability adapted by [1]

    def Move(self):
        sc = (self.currentPos.x, self.currentPos.y)
        ec = (self.target.x, self.target.y)
        path = self.Dijkstra(sc, ec)

        direction = vec(path[0][0] - self.currentPos.x, path[0][1] - self.currentPos.y)

        if (self.CanTurn(direction)):
            self.direction = direction            
        
