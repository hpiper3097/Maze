from adjacency_list import *
from random import choice, randint
from maze_animation import MazeAnimator

def loop_erased_walk(nj, compare_to_list, nodes):
    #initialize path with starting val
    path = [nj]
    #randomly select next node from adjacency list
    n0 = choice(nodes[path[-1]].get_list())
    path.append(n0)

    #until we find a node we already have, continue walking
    while n0 in compare_to_list:
        n0 = choice(nodes[path[-1]].get_list())
        path.append(n0)

    #create final list of node objects and initialize their adjacency lists
    npath = []
    for n in path:
        npath.append(Node(n))

    npath[0].update_by_list([path[1]])
    npath[-1].update_by_list([path[-2]])

    for i in range(1, len(path)-1):
        npath[i].update_by_list([path[i-1], path[i+1]] + npath[i].get_list())
        if path.count(path[i]) == 1:
            continue
        cnt = path.count(path[i])
        ind = path.index(path[i]) + 1 
        for _ in range(cnt - 1):
            ind = path.index(path[i], ind)
            npath[ind].update_by_list(npath[ind].get_list() + [path[i-1], path[i+1]])
            ind += 1

    #remove loops from path
    for n in path:
        if path.count(n) > 1:
            path.reverse()
            npath.reverse()
            for _ in range(path.count(n)-1):
                npath.pop(path.index(n))
                path.remove(n)
            npath.reverse()
            path.reverse()

    for n in npath:
        li = []
        for m in n.get_list():
            if m not in li:
                li.append(m)
        n.update_by_list(li)

    return npath

#wilson's algorithm to generate a uniform spanning tree
#accepts a list of nodes as input
def wilsons_algorithm(g, start=-1):
    nk = randint(0, len(g)-1)
    if start != -1:
        nk = start
    uni_span_tree = [Node(nk)]
    #uni_span_tree_c is just a list of the values of nodes which are not yet present in uni_span_tree
    uni_span_tree_c = [x for x in range(0, len(g))]
    uni_span_tree_c.remove(nk)
    while uni_span_tree_c:
        nj = choice(uni_span_tree_c)
        new_path = loop_erased_walk(nj, uni_span_tree_c, g)
        new_path.reverse()
        ind = 0
        for n in uni_span_tree:
            if n.val == new_path[0].val:
                ind = uni_span_tree.index(n)
                n.update_by_list(new_path[0].get_list() + n.get_list()) 
                break
        new_path.pop(0)
        uni_span_tree = uni_span_tree[:ind+1] + new_path + uni_span_tree[ind+1:]
        for n in new_path:
           uni_span_tree_c.remove(n.val)
    return uni_span_tree

#driver code
def main():
    rows = 6
    cols = rows
    pl = Plane2D(rows, cols)
    ust = wilsons_algorithm(pl.nodes)
    ustGraph = Graph(rows*cols)

    for n in ust:
        ustGraph.addNode(n)

    def co(n):
        return 2*n+1
    
    mz2 = []
    mz2.append(np.zeros(co(cols), dtype=np.int8))
    i = 0
    for i in range(rows):
        li = [0]
        for j in range(cols):
            li.append(0)
            li.append(0)
        mz2.append(np.array(li)) 
        mz2.append(np.zeros(co(cols), dtype=np.int8))
    mz2 = np.array(mz2)
    
    for u in ust:
        temp_row = int(u.val/cols)
        temp_col = u.val%cols
        mz2[co(temp_row), co(temp_col)] = 1
        for j in u.get_list():
            tr = int(j/cols)
            tc = j%cols
            if mz2[co(tr), co(tc)] == 1: 
                continue
            if abs(u.val - j) == 1:
                if j < u.val:
                    mz2[co(tr), co(tc) + 1] = 1
                    continue
                mz2[co(tr), co(tc) - 1] = 1
                continue
            if j < u.val:
                mz2[co(tr) + 1, co(tc)] = 1
                continue
            mz2[co(tr) - 1, co(tc)] = 1
        
    for i in range(1, co(cols)-1):
        if mz2[1, i] == 1:
            mz2[0, i] = 1
            break
        
    for i in range(co(cols)-2, 0, -1):
        if mz2[rows-2, i] == 1:
            mz2[co(rows)-1, i] = 1
            break
        
    mAnim = MazeAnimator()
    mAnim.set_maze(mz2)
    mAnim.render()

if __name__ == '__main__':
    from plane2D import Plane2D
    import numpy as np
    main()