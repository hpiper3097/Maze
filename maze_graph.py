from graph import *
from dataclasses import dataclass, field
from enum import Enum, auto

#for weighting wall to node nonzero
global bigNum
BIGNUM = 1000

class NodeType(Enum):
    #Type of Node in Maze

    EMPTY = auto()
    WALL = auto()
    CELL = auto()
    START = auto()
    EXIT = auto()

@dataclass
class MazeNode(Node):
    nodeType: NodeType = field(default=NodeType.EMPTY)

    def setNodeType(self, nt: NodeType):
        self.nodeType = nt

    def printNode(self, End=''):
        print(f'({self.x},{self.y}  type={self.nodeType})', end=End)

@dataclass
class MazeEdge(Edge):
    source: MazeNode
    destination: MazeNode

    def __post_init__(self):
        self.initWeights()
        self.update()

    def update(self):
        if (self.source.nodeType != self.destination.nodeType):
            self.weight = BIGNUM

    def mazeEdgePrint(self):
        self.source.printNode()
        self.destination.printNode(End='\n')

class MazeGraph(Graph):

    #split into nodes[] init and edges[] init
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes = []
        self.edges = {}
        self.update()

    def update(self):
        self.init_node_arr()
        self.init_edge_dict()

    #fill self.node 
    def init_node_arr(self):
        #init nodes, the 'maze' structure
        lix = [x for x in range(self.height)]
        liy = [y for y in range(self.width)]
        for y in liy:
            for x in lix:
                # i have swapped x and y here instead of swapping them in many other places :^)
                self.nodes.append(MazeNode(x=y, y=x))

    def init_edge_dict(self):
        for src in self.nodes:
            #only creating list of nodes which have an edge of weight 1 with source node
            srcEdges = [des._id for des in self.nodes if MazeEdge(src, des).weight == 1]
            self.edges[src._id] = srcEdges

#driver code
def main():
    gr = MazeGraph(3, 4)
    gr.printEdges()

if __name__ == '__main__':
    main()