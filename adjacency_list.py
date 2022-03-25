#adjacency list implementation
#Node.update() allows filling the adjacency_list via func

class Graph:
    def __init__(self, nodes):
        self.N = nodes
        self.graph = {}

    def addNode(self, n):
        self.graph[n.val] = n

    def __hasCycles(self, v, visited, parent):
        visited[v] = True 
        for i in self.graph[v].get_list():
            if visited[i] == False:
                if self.__hasCycles(i, visited, v):
                    return True
                elif parent != i:
                    return True
        return False
         
    def hasCycles(self):
        visited = [False]*(self.V)
        for i in range(self.N):
            if visited[i] == False:
                if self.__hasCycles(i, visited, -1) == True:
                    return True
        return False

    def removeCycles(self):
        pass

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
    def __init__(self, u, v):
        self.u = u
        self.v = v