import collections

from more_itertools import adjacent
from node import Node
class DFS:
    def __init__(self, root, n):
        self.s = set()
        self.root = root
        self.N = n
        self.queue = collections.deque()
        self.changColor(self.root, 1)

    def changColor(self, node, color):
        node.color = color

    def increseDistanc(self, node):
        node.destanc += 1
    
    def dfsSolve(self):
        stnode = Node(self.root)
        self.queue.append(stnode)
        self.s.add(stnode.step)
        

        while len(self.queue)!=0:
            u = self.queue.pop()
            if u.solved:
                return u.solutionPath

            if u.color==0:
                self.DFS_VIST(u)
                
        
    def DFS_VIST(self,node):
        
        self.changColor(node,1)
        self.increseDistanc(node)
        adj =self.getAdj(node)

        for v in adj:
            if node.solved:
                return node.solutionPath
            if v.color==0:
                self.queue.append(v)
                self.DFS_VIST(v)

        self.changColor(node,2)


    def getAdj(self, node):
        l = []
        for move, action in node.actions:
            child = Node(move(), node, action)
            if child.step not in self.s:
                self.s.add(child.step)
                l.append(child)
        return l