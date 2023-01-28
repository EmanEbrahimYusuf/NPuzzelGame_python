import collections


from node import Node

class BFS:
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

    def bfsSolve(self):
        stnode = Node(self.root)
        self.queue.append(stnode)
        self.s.add(stnode.step)
        while len(self.queue) != 0:
            u = self.queue.popleft()
            if u.solved:
                return u.solutionPath

            adj=self.getAdj(u)

            for i in adj:
                if i.color == 0:
                    self.changColor(i,1)
                    self.increseDistanc(i)
                    self.queue.append(i)

            u.color = 2

    def getAdj(self, node):
        l = []
        for move, action in node.actions:
            child = Node(move(), node, action)
            if child.step not in self.s:
                self.s.add(child.step)
                l.append(child)
        return l
