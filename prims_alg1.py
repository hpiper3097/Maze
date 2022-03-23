import numpy as np
from random import choice, randint

def prims_bool(r, c):
    rows = r
    cols = c

    mz = np.zeros((rows, cols), dtype=np.int8)

    mz_hist = []
    mz_hist.append(mz.copy())

    x = randint(1, rows-2)
    y = randint(1, cols-2)
    mz[x, y] = 1

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
        #update maze history
        if not np.array_equal(mz_hist[-1], mz):
            mz_hist.append(mz.copy())
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

    if not np.array_equal(mz_hist[-1], mz):
        mz_hist.append(mz.copy())
    
    return mz_hist


#driver code
def main():
    rows = 50
    cols = rows
    mz = prims_bool(rows, cols)
    mzf = np.stack(mz, axis=2)
    print(np.shape(mzf))
    print(len(mzf))

    from matplotlib import pyplot as plt, animation

    t = np.arange(len(mz))
    x = np.arange(rows+1)
    y= np.arange(cols+1)

    fig, ax = plt.subplots()
    fig.canvas.set_window_title('Maze!')
    ax.set_title('still a shit maze haha')
    cax = ax.pcolormesh(mzf[:, :, -1], vmin=0, vmax=3)
    fig.colorbar(cax)

    def animate(i):
        cax.set_array(mzf[:, :, i].flatten())

    anim = animation.FuncAnimation(fig, animate, interval=8, frames=len(t))
    anim.save('mazegen.mp4')
#    plt.xticks([])
#    plt.yticks([])

    plt.draw()
    plt.show()

if __name__ == '__main__':
    main()