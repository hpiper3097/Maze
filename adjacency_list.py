#adjacency list implementation
#Node.update() allows filling the adjacency_list via func
class Node:
    def __init__(self, val):
        self.adjacency_list = []
        self.val = val

    def update_by_list(self, adj):
        self.adjacency_list = adj

    def update_by_function(self, func, i):
        func(self.adjacency_list, i)

    def append_by_list(self, adj):
        self.adjacency_list.append(adj)

    def get_list(self):
        return self.adjacency_list

class Edge:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2