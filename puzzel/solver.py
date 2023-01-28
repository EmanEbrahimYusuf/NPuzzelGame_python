
import numpy as np
import heapq
from queue import PriorityQueue 
import heapq 
from node import Node
class Solver:
    j=0
    def __init__(self, start, N):
        self.start = start
        self.N = N
        self.seen=set()
        
    
    def getNextLevel(self , parent):
        prQ=PriorityQueue()
        for move, action in parent.actions:
            child = Node(move(), parent, action)
            self.j-=1
            prQ.put((child.f,self.j,(child,parent)))
        return prQ

    def solve(self):
        i=1
        #fibonachiHeap
        pq = PriorityQueue()
        stnode = Node(self.start)
        pq.put((stnode.f,0,stnode))
        self.seen.add(stnode.step)
        while not pq.empty():
            node = pq.get()[2]
            if node.solved:
                return node.solutionPath
            for move, action in node.actions:
                child = Node(move, node, action)
                if child.step not in self.seen:
                    i=i-1
                    pq.put((child.f,i,child))
                    self.seen.add(child.step)
                
            
            


    # -------------------------------------------------------------------------

    def getInvCount(self, arr):
        inv_count = 0
        empty_value = -1
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                if (arr[i] < arr[j]):
                    inv_count += 1

        return inv_count

    def get0Index(self, puzzle):
        for (y, row) in enumerate(puzzle):
            for x, value in enumerate(row):
                if (value == 0):
                    return (y, x)

    def isSolveble(self, puzzle):
        zeroLocation = self.get0Index(puzzle)
        yIsEven = False
        if zeroLocation[0] % 2 == 0:
            yIsEven = True
        else:
            yIsEven = False

        inversEven = False
        l = []
        for i in puzzle:
            for j in i:
                if j != 0:
                    l.append(j)
        inversion_count = 0
        for index, value in enumerate(l):
            for value_to_compare in l[index + 1: len(l)]:
                if value > value_to_compare:
                    inversion_count += 1

        invCount = inversion_count

        if invCount % 2 == 0:
            inversEven = True
        else:
            inversEven = False
        widthEven = False
        if self.N % 2 == 0:
            widthEven = True
        else:
            widthEven = False

        if widthEven:
            zero_odd = not yIsEven

        return ((not widthEven and inversEven)
                or
                (widthEven and (zero_odd == inversEven)))
