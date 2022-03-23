import numpy as np
from random import choice, randint

def prims_bool():
    rows = 20
    cols = 20 

    mz = np.zeros((rows, cols), dtype=np.int8)
    mz_visited = np.zeros((rows, cols), dtype=np.int8)

    x = randint(1, rows-2)
    y = randint(1, cols-2)
    mz[x, y] = 1
    mz_visited[x, y] = 1

    walls = []
    walls.append((x-1, y))
    walls.append((x+1, y))
    walls.append((x, y-1))
    walls.append((x, y+1))

    for w in walls:
        mz[w[0], w[1]] = 2

    def sCel(x, y):
        sc = 0
        if mz[x - 1, y] == 1:
            sc += 1
        if mz[x + 1, y] == 1:
            sc += 1
        if mz[x, y - 1] == 1:
            sc += 1
        if mz[x, y + 1] == 1:
            sc += 1

        return sc

    while walls:
        #pick a random wall
        ran_wall = choice(walls)
        assert(walls.count(ran_wall) == 1)
        x = ran_wall[0]
        y = ran_wall[1]

        #check if its a left wall
        if y != 0:
            #
            # ? w c
            #
            if mz[x, y-1] == 0 and mz[x, y+1] == 1:
                if sCel(x, y) < 2:
                    #denote the new path
                    mz[x, y] = 1
                    mz_visited[x, y] = 1

                    #mark new walls
                    #upper cell
                    if x != 0:
                        if mz[x-1, y] != 1:
                            mz[x-1, y] = 2
                        if (x-1, y) not in walls:
                            walls.append((x-1, y))
                    #bottom cell
                    if x != rows - 1:
                        if mz[x+1, y] != 1:
                            mz[x+1, y] = 2
                        if (x+1, y) not in walls:
                            walls.append((x+1, y))
                    #leftmost cell
                    if mz[x, y-1] != 1:
                        mz[x, y-1] = 2
                    if (x, y-1) not in walls:
                        walls.append((x, y-1))

                for w in walls:
                    if (w[0] == x and w[1] == y):
                        walls.remove(w)
                continue
                            
        #check if its a right wall
        if y != cols-1:
            #
            # c w ?
            #
            if mz[x, y+1] == 0 and mz[x, y-1] == 1:
                if sCel(x, y) < 2:
                    #denote the new path
                    mz[x, y] = 1
                    mz_visited[x, y] = 1

                    #mark new walls
                    #upper cell
                    if x != 0:
                        if mz[x-1, y] != 1:
                            mz[x-1, y] = 2
                        if (x-1, y) not in walls:
                            walls.append((x-1, y))
                    #bottom cell
                    if x != rows - 1:
                        if mz[x+1, y] != 1:
                            mz[x+1, y] = 2
                        if (x+1, y) not in walls:
                            walls.append((x+1, y))
                    #rightmost cell
                    if mz[x, y+1] != 1:
                        mz[x, y+1] = 2
                    if (x, y+1) not in walls:
                        walls.append((x, y+1))

                for w in walls:
                    if (w[0] == x and w[1] == y):
                        walls.remove(w)
                continue
                            
        #check if its a upper wall
        if x != 0:
            #   ?
            #   w  
            #   c
            if mz[x-1, y] == 0 and mz[x+1, y] == 1:
                if sCel(x, y) < 2:
                    #denote the new path
                    mz[x, y] = 1
                    mz_visited[x, y] = 1

                    #mark new walls
                    #leftmost cell
                    if y != 0:
                        if mz[x, y-1] != 1:
                            mz[x, y-1] = 2
                        if (x, y-1) not in walls:
                            walls.append((x, y-1))
                    #rightmost cell
                    if y != cols-1:
                        if mz[x, y+1] != 1:
                            mz[x, y+1] = 2
                        if (x, y+1) not in walls:
                            walls.append((x, y+1))
                    #upper cell
                    if mz[x-1, y] != 1:
                        mz[x-1, y] = 2
                    if (x-1, y) not in walls:
                        walls.append((x-1, y))

                for w in walls:
                    if (w[0] == x and w[1] == y):
                        walls.remove(w)
                continue
                            
        #check if its a lower wall
        if x != rows-1:
            #   c
            #   w  
            #   ?
            if mz[x+1, y] == 0 and mz[x-1, y] == 1:
                if sCel(x, y) < 2:
                    #denote the new path
                    mz[x, y] = 1
                    mz_visited[x, y] = 1

                    #mark new walls
                    #leftmost cell
                    if y != 0:
                        if mz[x, y-1] != 1:
                            mz[x, y-1] = 2
                        if (x, y-1) not in walls:
                            walls.append((x, y-1))
                    #rightmost cell
                    if y != cols-1:
                        if mz[x, y+1] != 1:
                            mz[x, y+1] = 2
                        if (x, y+1) not in walls:
                            walls.append((x, y+1))
                    #lower cell
                    if mz[x+1, y] != 1:
                        mz[x+1, y] = 2
                    if (x+1, y) not in walls:
                        walls.append((x+1, y))

                for w in walls:
                    if (w[0] == x and w[1] == y):
                        walls.remove(w)
                continue

        for w in walls:
            if (w[0] == x and w[1] == y):
                walls.remove(w)

    for i in range(rows):
        for j in range(cols):
            if mz[i, j] == 0:
                mz[i, j] = 2
                            
    for n in range(1, cols-1):
        if mz[1, n] == 1:
            mz[0, n] = 1
            break

    for n in range(cols-2, 0, -1):
        if mz[rows-2, n] == 1:
            mz[rows-1, n] = 1
            break

    return mz


#driver code
def main():
    mz = prims_bool()
    import matplotlib.pyplot as plt
    plt.pcolormesh(mz)
#    plt.xticks([])
#    plt.yticks([])
    plt.show()

if __name__ == '__main__':
    main()