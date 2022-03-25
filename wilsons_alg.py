from adjacency_list import *
from random import choice, randint

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
def wilsons_algorithm(g):
    nk = 5
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
    pl = Plane2D(4, 5)
    ust = wilsons_algorithm(pl.nodes)
    print('OUTPUT::')
    for n in ust:
        print(f'node: {n.val}\tadj: {n.get_list()}\t og: {pl.nodes[n.val].get_list()}')

if __name__ == '__main__':
    from plane2D import Plane2D
    main()