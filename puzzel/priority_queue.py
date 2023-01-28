
from node import Node
import math


class Priority__Queue:
    def __init__(self):
        self.data = []
        self.cost = []

    def insert(self, node):
        f = node.f
        node = node
        min = 100000000000000000
        pos = 0
        if len(self.data) == 0:
            self.data.append(node)
            self.cost.append(f)

        else:
            for x, i in self.cost, range(0, len(self.cost)):
                if min > x:
                    pos = i
                else:
                    continue
            self.data.insert(pos, node)
            self.cost.insert(pos, f)
            print(self.data)

    def pop(self):
        try:
            min = 0
            for i in range(len(self.cost)):
                if self.cost[i] < self.cost[min]:
                    min = i
            item = self.data[min]
            f = self.cost[min]
            del self.data[min]
            del self.cost[min]
            return (item, f)
        except IndexError:
            print()
            exit()

    def printData(self):
        print(self.data)

    def printCosts(self):
        print(self.cost)

    def printLen(self):
        print(len(self.data))

# A simple implementation of Priority Queue
# using Queue.


class Priority_Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    
    def isEmpty(self):
        return len(self.queue) == 0

    
    def insert(self, data):
        self.queue.append(data)

    
    def delete(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i].f < self.queue[min].f:
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item
        except IndexError:
            print()
            exit()
