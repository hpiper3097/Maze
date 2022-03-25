from adjacency_list import *

class Plane2D:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.nodes = []
        for i in range(self.rows*self.cols):
            self.nodes.append(Node(i))
            self.nodes[i].update_by_function(self.node_list_init, i)

    def node_list_init(self, adj_li, i):
        if (i > self.cols-1):
            adj_li.append(i-self.cols)
        if (i < (self.rows-1)*self.cols):
            adj_li.append(i+self.cols)
        if (i % self.cols != 0):
            adj_li.append(i-1)
        if (i % self.cols != self.cols-1):
            adj_li.append(i+1)
        
#driver code
def main():
    pl = Plane2D(3, 3)
    for i in range(9):
        print(f'{i}:\t{pl.nodes[i].adjacency_list}')

if __name__ == '__main__':
    main()