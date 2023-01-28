class Node:

    def __init__(self, puzzle, parent=None, action=None,color=0,destanc=0):
        self.puzzle = puzzle
        self.parent = parent
        self.action = action
        self.color=color
        self.destanc=destanc
        if (self.parent != None):
            self.g =parent.g +1
        else:
            self.g = 0
            

    @property
    def AstarScore(self):
        f = self.g+self.h
        return f

    @property
    def step(self):
        return str(self)
    @property
    def solutionPath(self):
        node = self
        p = []
        while node:
            p.append(node)
            node = node.parent
        return reversed(p)

    @property
    def solved(self):
        return self.puzzle.solved

    @property
    def actions(self):
        return self.puzzle.actions2

    @property
    def h(self):
        return self.puzzle.hammingDistance

    @property
    def f(self):
        return self.h + self.g

    def __str__(self):
        return str(self.puzzle)