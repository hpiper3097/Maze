import itertools
import numpy as np
from dataclasses import dataclass, field

#Classes to represent a graph structure for a multitude of applications

@dataclass
class Node:
    x: int
    y: int
    _id_iter: itertools.count() = itertools.count()
    _id: int = field(init=False, repr=True)

    def __post_init__(self):
        self._id = next(self._id_iter)

    def printNode(self, End=''):
        print(f'({self.x},{self.y})', end=End)

@dataclass
class Edge:
    source: Node
    destination: Node
    weight: int = 0

    def __post_init__(self):
        self.initWeights()

    def initWeights(self):
        if (self.source.x == self.destination.x and abs(self.source.y - self.destination.y) == 1):
            self.weight = 1
        elif (self.source.y == self.destination.y and abs(self.source.x - self.destination.x) == 1):
            self.weight = 1

class Graph:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.edges = dict()
        self.nodes = []
        self.update()

    def update(self):
        #fill nodes array
        lix = [x for x in range(self.width)]
        liy = [y for y in range(self.height)]
        for x in lix:
            for y in liy:
                self.nodes.append(Node(x=x, y=y))

        #fill edges dictionary
        for src in self.nodes:
            srcEdges = [des._id for des in self.nodes if Edge(src, des).weight == 1]
            self.edges[src._id] = srcEdges

    def coordsToID(self, x, y):
        for _id, nd in enumerate(self.nodes):
            if (nd.x == x and nd.y == y):
                return _id
        return None

    def at(self, x, y):
        return self.nodes[self.coordsToID(x, y)]

    def printEdges(self):
        for k,v in self.edges.items():
            print(f'src: {k}\treaches: {v}')

#driver code
def main():
    gr = Graph(3, 3)
    gr.printEdges()
    print(f'(1, 2) at id={gr.at(1, 2)}')

if __name__ == '__main__':
    main()