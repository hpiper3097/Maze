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
        mz_visited[w[0], w[1]] = 1

    def sCel(x, y):
        sc = 0
        if x != 0:
            if (mz[x-1, y] == 1):
                sc += 1
        if x != rows-1:
            if (mz[x+1, y] == 1):
                sc += 1
        if y != 0:
            if (mz[x, y-1] == 1):
                sc += 1
        if y != cols-1:
            if (mz[x, y+1] == 1):
                sc += 1
        return sc

    while walls:
        ran_wall = choice(walls)
        x = ran_wall[0]
        y = ran_wall[1]

        #case 1
        if x != 0 and x != rows-1:
            if mz[x-1, y] == 1:
                if sCel(x, y) < 2:
                    mz[x, y] = 1
                    if x != rows-1:
                        if mz_visited[x+1, y] == 0:
                            mz_visited[x+1, y] = 1
                            walls.append((x+1, y))
                    if y != 0:
                        if mz_visited[x, y-1] == 0:
                            mz_visited[x, y-1] = 1 
                            walls.append((x, y-1))
                    if y != cols-1:
                        if mz_visited[x, y+1] == 0:
                            mz_visited[x, y+1] = 1
                            walls.append((x, y+1))
                    walls.remove(ran_wall)
                    continue
        #case 2
        if x != rows - 1:
            if mz[x+1, y] == 1:
                if sCel(x, y) < 2:
                    mz[x, y] = 1
                    if x != 0:
                        if mz_visited[x-1, y] == 0:
                            mz_visited[x-1, y] = 1
                            walls.append((x-1, y))
                    if y != 0:
                        if mz_visited[x, y-1] == 0:
                            mz_visited[x, y-1] = 1 
                            walls.append((x, y-1))
                    if y != cols-1:
                        if mz_visited[x, y+1] == 0:
                            mz_visited[x, y+1] = 1
                            walls.append((x, y+1))
                    walls.remove(ran_wall)
                    continue
        #case 3
        if y != 0:
            if mz[x, y-1] == 1:
                if sCel(x, y) < 2:
                    mz[x, y] = 1
                    if x != 0:
                        if mz_visited[x-1, y] == 0:
                            mz_visited[x-1, y] = 1
                            walls.append((x-1, y))
                    if x != rows-1:
                        if mz_visited[x+1, y] == 0:
                            mz_visited[x+1, y] = 1
                            walls.append((x+1, y))
                    if y != 0:
                        if mz_visited[x, y-1] == 0:
                            mz_visited[x, y-1] = 1 
                            walls.append((x, y-1))
                    walls.remove(ran_wall)
                    continue
        #case 4
        if y != cols - 1:
            if mz[x, y+1] == 1:
                if sCel(x, y) < 2:
                    mz[x, y] = 1
                    if x != 0:
                        if mz_visited[x-1, y] == 0:
                            mz_visited[x-1, y] = 1
                            walls.append((x-1, y))
                    if x != rows-1:
                        if mz_visited[x+1, y] == 0:
                            mz_visited[x+1, y] = 1
                            walls.append((x+1, y))
                    if y != cols-1:
                        if mz_visited[x, y+1] == 0:
                            mz_visited[x, y+1] = 1 
                            walls.append((x, y+1))
                    walls.remove(ran_wall)
                    continue

        if ran_wall in walls:
            walls.remove(ran_wall)
    
    #for unv in mz_visited: 
    #    for e in unv:
    #        if e == 0:
    #            e = 1

    #for n in range(1, cols):
    #    if mz[1, n] == 1:
    #        mz[0, n] = 1
    #        break

    #for n in range(cols-1, 0, -1):
    #    if mz[rows-2, n] == 1:
    #        mz[rows-1, n] = 1
    #        break

    return mz


#driver code
def main():
    mz = prims_bool()
    import matplotlib.pyplot as plt
    plt.pcolormesh(mz)
    plt.xticks([])
    plt.yticks([])
    plt.show()

if __name__ == '__main__':
    main()