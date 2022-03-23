#imports
import random
import time
from colorama import init, Fore
from tkinter import *

init()

def print_maze(maze):
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze[i][j] == 'u':
                print(Fore.WHITE, f'{chr(9609)}', end="")
            elif maze[i][j] == 'c':
                print(Fore.GREEN, f'{chr(9609)}', end="")
            else:
                print(Fore.MAGENTA, f'{chr(9609)}', end="")
        print('\n')

def surroundingCells(rand_wall):
    s_cells=0
    if (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
        s_cells += 1
    return s_cells

#gen maze given dimensions
def init_maze(width, height):
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append('u')
        maze.append(line)

#fill in the walls and cells of the maze
def create_maze(width, height):

    starting_height = int(random.choice(range(0, height)))
    starting_width = int(random.choice(range(0, width)))
    if starting_height == 0:
        starting_height += 1
    if starting_height == height-1:
        starting_height -= 1
    if starting_width == 0:
        starting_width += 1
    if starting_width == width-1:
        starting_width -= 1

    print(str(starting_height) + ' ' + str(starting_width) + ':)')
    maze[starting_height][starting_width] = cell
    walls = []
    walls.append([starting_height-1, starting_width])
    walls.append([starting_height, starting_width+1])
    walls.append([starting_height, starting_width-1])
    walls.append([starting_height+1, starting_width])

    #set starting walls
    maze[starting_height-1][starting_width] = 'w'
    maze[starting_height][starting_width+1] = 'w'
    maze[starting_height][starting_width-1] = 'w'
    maze[starting_height+1][starting_width] = 'w'

    while walls:
        #select random wall
        rand_wall = walls[random.choice(range(0, len(walls)))]

        #check if it's a left wall
        if rand_wall[1] != 0:
            if maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == 'c':
                #get number of surrounding cells
                s_cells = surroundingCells(rand_wall)
                if s_cells < 2:
                    #new path
                    maze[rand_wall[0]][rand_wall[1]] = 'c'

                    #set new walls
                    #upper cell
                    if rand_wall[0] != 0:
                        if maze[rand_wall[0]-1][rand_wall[1]] != 'c':
                            maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                        if [rand_wall[0]-1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0]-1, rand_wall[1]])
                    
                    #bottom cell
                    if rand_wall[0] != height-1:
                        if maze[rand_wall[0]+1][rand_wall[1]] != 'c':
                            maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                        if [rand_wall[0]+1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0]+1, rand_wall[1]])

                    maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                    if [rand_wall[0], rand_wall[1]-1] not in walls:
                        walls.append([rand_wall[0], rand_wall[1]-1])

                #delete wall
                for wall in walls:
                    if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                        walls.remove(wall)

                continue
                    
        #check if it's a right wall 
        if rand_wall[1] != width-1:
            if maze[rand_wall[0]][rand_wall[1]-1] == 'c' and maze[rand_wall[0]][rand_wall[1]+1] == 'u':

                s_cells = surroundingCells(rand_wall)
                if s_cells < 2:
                    #new path
                    maze[rand_wall[0]][rand_wall[1]] = 'c'

                    #set new walls
                    if rand_wall[0] != 0:
                        if maze[rand_wall[0]-1][rand_wall[1]] != 'c':
                            maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                        if [rand_wall[0]-1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0]-1, rand_wall[1]])

                    if rand_wall[0] != height-1:
                        if maze[rand_wall[0]+1][rand_wall[1]] != 'c':
                            maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                        if [rand_wall[0]+1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0]+1, rand_wall[1]])

                    maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                    if [rand_wall[0], rand_wall[1]+1] not in walls:
                        walls.append([rand_wall[0], rand_wall[1]+1])

                for wall in walls:
                    if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                        walls.remove(wall)
                continue
                        

        #check it's not an upper wall
        if rand_wall[0] != 0:
            if maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == 'c':

                s_cells = surroundingCells(rand_wall)
                if s_cells < 2:
                    #create new path
                    maze[rand_wall[0]][rand_wall[1]] = 'c'


                    if rand_wall[1] != 0:
                        if maze[rand_wall[0]][rand_wall[1]-1] != 'c':
                            maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                        if [rand_wall[0], rand_wall[1]-1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1]-1])

                    if rand_wall[1] != width-1:
                        if maze[rand_wall[0]][rand_wall[1]+1] != 'c':
                            maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                        if [rand_wall[0], rand_wall[1]+1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1]+1])

                    maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                    if [rand_wall[0]-1, rand_wall[1]] not in walls:
                        walls.append([rand_wall[0]-1, rand_wall[1]])

                for wall in walls:
                    if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                        walls.remove(wall)
                continue

        #check if its a bottom wall
        if rand_wall[0] != height-1:
            print(f'{len(maze)} : {len(maze[0])}')
            if maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == 'c':
    
                s_cells = surroundingCells(rand_wall)
                if s_cells < 2:
                    #add new path
                    maze[rand_wall[0]][rand_wall[1]] = 'c'

                    if rand_wall[1] != 0:
                        if maze[rand_wall[0]][rand_wall[1]-1] != 'c':
                            maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                        if [rand_wall[0], rand_wall[1]-1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1]-1])

                    if rand_wall[1] != width-1:
                        if maze[rand_wall[0]][rand_wall[1]+1] != 'c':
                            maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                        if [rand_wall[0], rand_wall[1]+1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1]+1])

                    maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                    if [rand_wall[0]+1, rand_wall[1]] not in walls:
                        walls.append([rand_wall[0]+1, rand_wall[1]])

                for wall in walls:
                    if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                        walls.remove(wall)
                continue

        for wall in walls:
            if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                walls.remove(wall)
            
#fill in the spots we missed
def fill_walls(width, height):
    for i in range(0, height):
        for j in range(0, width):
            if maze[i][j] == 'u':
                maze[i][j] = 'w'

#create entrance and exit
def add_entrance_exit(width, height):
    for i in range(0, width):
        if maze[1][i] == 'c':
            maze[0][i] = 'c'
            break
    for i in range(width-1, 0, -1):
        if maze[height-2][i] == 'c':
            maze[height-1][i] = 'c'
            break

def applyNoise(noise):
    n = 1.0 - float(noise)/100.0
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze[i][j] == 'w':
                var = random.random()
                if n <= var:
                    print(str(n) + ' is <= ' + str(var))
                    maze[i][j] = 'c'

#render the maze to the window
def renderToApp():
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            lbl = Label(App, background=colorDict[maze[i][j]], width=2, height=1)
            lbl.grid(row=i+1, column=j+1)
        lbl = Label(App, background='black', width=2, height=1)
        lbl.grid(row=i+1, column=len(maze[0])+1)
    for j in range(0, len(maze[0])+2):
        lbl = Label(App, background='black', width=2, height=1)
        lbl.grid(row=len(maze)+1, column=j)

#render interactable UI elements
def renderUI(xV, yV, nV):
    B = Button(App, text='Generate', command=generate, width=8)

    xL = Label(App, text='Width: ', width=6)
    xVal = IntVar()
    xE = Scale(App, from_=16, to=55, width=16, variable=xVal, orient=HORIZONTAL)
    xE.set(xV)

    yL = Label(App, text='Height: ', width=6)
    yVal = IntVar()
    yE = Scale(App, from_=16, to=30, width=16, variable=yVal, orient=HORIZONTAL)
    yE.set(yV)

    nL = Label(App, text='Noise: ', width=6)
    nVal = IntVar()
    nE = Scale(App, from_=0, to=100, width=20, variable=nVal, orient=HORIZONTAL)

    B.grid(row=0, column=0, columnspan=4)
    xL.grid(row=0, column=5, columnspan=3)
    xE.grid(row=0, column=8, columnspan=8)
    yL.grid(row=0, column=17, columnspan=3)
    yE.grid(row=0, column=20, columnspan=8)
    nL.grid(row=0, column=29, columnspan=3)
    nE.grid(row=0, column=32, columnspan=10)

#clear screen
def clear():
   li = App.grid_slaves() 
   for l in li:
       l.destroy()

#function for button
def generate():

    for i in range(0, height):
        for j in range(0, width):
            maze[i][j] = 'u'

    wid = int(xVal.get())
    hei = int(yVal.get())
    noi = int(nVal.get())

    clear()
    renderUI(wid, hei, noi)

    create_maze(wid, hei)
    fill_walls(wid, hei)
    add_entrance_exit(wid, hei)
    applyNoise(noi)
    print_maze(maze)

    renderToApp()

App = Tk()
App.title('Maze Generator')
App['background'] = 'black'

colorDict = {'w':'red', 'c':'green', 'u':'green', 'x':'red'}

cell = 'c'
wall = 'w'
height = 30
width = 50
noise = 0
maze = []

init_maze(width, height)
create_maze(width, height)
fill_walls(width, height)
add_entrance_exit(width, height)
applyNoise(noise)
print_maze(maze)

B = Button(App, text='Generate', command=generate, width=8)
xL = Label(App, text='Width: ', width=6)
yL = Label(App, text='Height: ', width=6)
nL = Label(App, text='Noise: ', width=6)
xVal = IntVar()
yVal = IntVar()
nVal = IntVar()
yE = Scale(App, from_=16, to=30, width=16, variable=yVal, orient=HORIZONTAL)
xE = Scale(App, from_=16, to=55, width=16, variable=xVal, orient=HORIZONTAL)
nE = Scale(App, from_=0, to=100, width=20, variable=nVal, orient=HORIZONTAL)

xE.set(width)
yE.set(height)
nE.set(noise)

B.grid(row=0, column=0, columnspan=4)
xL.grid(row=0, column=5, columnspan=3)
xE.grid(row=0, column=8, columnspan=8)
yL.grid(row=0, column=17, columnspan=3)
yE.grid(row=0, column=20, columnspan=8)
nL.grid(row=0, column=29, columnspan=3)
nE.grid(row=0, column=32, columnspan=10)

renderToApp()

App.mainloop()
