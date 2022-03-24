#adjacency list implementation
#Node.update() allows filling the adjacency_list via func
class Node:
    def __init__(self):
        self.adjacency_list = []

    def update(self, func, i):
        func(self.adjacency_list, i)

class Edge:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2