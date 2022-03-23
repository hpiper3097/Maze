from maze_graph import *
from random import choice

global xlen, ylen

def print_maze(maze: MazeGraph):
    from colorama import init, Fore
    c = chr(9608)
    init()
    for n in maze.nodes:
        if (n.y == 0):
            print()
        if (n.nodeType == NodeType.CELL):
            print(Fore.LIGHTYELLOW_EX, f'{c}', end='')
        elif (n.nodeType == NodeType.WALL):
            print(Fore.BLUE, f'{c}', end='')
        else:
            print(Fore.LIGHTBLACK_EX, f'{c}', end='')
    

#externally validate xl and yl are > 5
def simplePrims(maze: MazeGraph):
    #choose point to start at
    x = choice([e for e in range(0, maze.width)])
    y = choice([e for e in range(0, maze.height)])
    #make sure we are not on an edge
    if (x == 0):
        x += 1
    if (y == 0):
        y += 1

    #set start position to CELL
    maze.at(x, y).setNodeType(NodeType.CELL)
    #initialize walls
    walls = maze.edges[maze.coordsToID(x, y)]
    #set nodes adjacent to CELL as WALL
    for wid in walls:
        maze.nodes[wid].setNodeType(NodeType.WALL)

    #function returns the number of adjacent points that are CELL
    def sCel(x: int, y: int):
        sc = 0
        if (maze.at(x-1, y).nodeType == NodeType.CELL):
            sc += 1
        if (maze.at(x+1, y).nodeType == NodeType.CELL):
            sc += 1
        if (maze.at(x, y-1).nodeType == NodeType.CELL):
            sc += 1
        if (maze.at(x, y+1).nodeType == NodeType.CELL):
            sc += 1
        return sc

    #until walls is empty, attempt to turn WALL into CELL
    while walls:
        #choose random wall from list
        ran_wall = walls[choice([e for e in range(0, len(walls))])]
        x = maze.nodes[ran_wall].x
        y = maze.nodes[ran_wall].y

        #check if ran_wall is a left WALL
        if (x != 0):
            #check if the WALL is between a CELL and EMPTY
            if (maze.nodes[maze.coordsToID(x-1, y)].nodeType == NodeType.EMPTY and maze.nodes[maze.coordsToID(x+1, y)].nodeType == NodeType.CELL):
                #get number of surrounding cells
                if (sCel(x, y) < 2):
                    #new path
                    maze.at(x, y).setNodeType(NodeType.CELL)
                #set new walls
                    #upper adjacent 
                    if (y != 0):
                        maze.at(x, y-1).setNodeType(NodeType.WALL)
                        if (maze.coordsToID(x, y-1) not in walls):
                            walls.append(maze.coordsToID(x, y-1))

                    #lower adjacent 
                    if (y != maze.height-1):
                        maze.at(x, y+1).setNodeType(NodeType.WALL)
                        if (maze.coordsToID(x, y+1) not in walls):
                            walls.append(maze.coordsToID(x, y+1))

                    #left adjacent 
                    maze.at(x-1, y).setNodeType(NodeType.WALL)
                    walls.append(maze.coordsToID(x-1, y))
                
                #delete wall
                walls.remove(ran_wall)
                continue

        #check if ran_wall is a right WALL
        if (x != maze.width-1):
            if (maze.nodes[maze.coordsToID(x+1, y)].nodeType == NodeType.EMPTY and maze.nodes[maze.coordsToID(x-1, y)].nodeType == NodeType.CELL):
                if (sCel(x, y) < 2):
                    maze.at(x, y).setNodeType(NodeType.CELL)
                    #upper adjacent 
                    if (y != 0):
                        maze.at(x, y-1).setNodeType(NodeType.WALL)
                        if (maze.coordsToID(x, y-1) not in walls):
                            walls.append(maze.coordsToID(x, y-1))
                    #lower adjacent 
                    if (y != maze.height-1):
                        maze.at(x, y+1).setNodeType(NodeType.WALL)
                        if (maze.coordsToID(x, y+1) not in walls):
                            walls.append(maze.coordsToID(x, y+1))
                    #upper adjacent 
                    maze.at(x+1, y).setNodeType(NodeType.WALL)
                    walls.append(maze.coordsToID(x+1, y))
                
                walls.remove(ran_wall)
                continue

        #check if ran_wall is a bottom WALL
        if (y != 0):
            if (maze.nodes[maze.coordsToID(x, y-1)].nodeType == NodeType.EMPTY and maze.nodes[maze.coordsToID(x, y+1)].nodeType == NodeType.CELL):
                if (sCel(x, y) < 2):
                    maze.at(x, y).setNodeType(NodeType.CELL)
                    #left adjacent 
                    if (x != 0):
                        maze.at(x-1, y).setNodeType(NodeType.WALL)
                        if (maze.coordsToID(x-1, y) not in walls):
                            walls.append(maze.coordsToID(x-1, y))
                    #right adjacent 
                    if (x != maze.width-1):
                        maze.at(x+1, y).setNodeType(NodeType.WALL)
                        if (maze.coordsToID(x+1, y) not in walls):
                            walls.append(maze.coordsToID(x+1, y))
                    #lower adjacent 
                    maze.at(x, y-1).setNodeType(NodeType.WALL)
                    walls.append(maze.coordsToID(x, y-1))
                
                walls.remove(ran_wall)
                continue

        #check if ran_wall is a upper WALL
        if (y != maze.height-1):
            if (maze.nodes[maze.coordsToID(x, y+1)].nodeType == NodeType.EMPTY and maze.nodes[maze.coordsToID(x, y-1)].nodeType == NodeType.CELL):
                if (sCel(x, y) < 2):
                    maze.at(x, y).setNodeType(NodeType.CELL)
                    #left adjacent 
                    if (x != 0):
                        maze.at(x-1, y).setNodeType(NodeType.WALL)
                        if (maze.coordsToID(x-1, y) not in walls):
                            walls.append(maze.coordsToID(x-1, y))
                    #right adjacent 
                    if (x != maze.width-1):
                        maze.at(x+1, y).setNodeType(NodeType.WALL)
                        if (maze.coordsToID(x+1, y) not in walls):
                            walls.append(maze.coordsToID(x+1, y))
                    #upper adjacent 
                    maze.at(x, y+1).setNodeType(NodeType.WALL)
                    walls.append(maze.coordsToID(x, y+1))
                
                walls.remove(ran_wall)
                continue

        if ran_wall in walls:
            walls.remove(ran_wall)

    for n in maze.nodes:
        if (n.nodeType == NodeType.EMPTY):
            n.setNodeType(NodeType.WALL)

    for n in range(0, maze.height):
        if (maze.at(1, n).nodeType == NodeType.CELL):
            maze.at(0, n).setNodeType(NodeType.CELL)
            break 

    for n in range(maze.height-1, 0, -1):
        if (maze.at(maze.width-2, n).nodeType == NodeType.CELL):
            maze.at(maze.width-1, n).setNodeType(NodeType.CELL)
            break

    return maze

#driver code
def main():
    height = 40
    width = 60

    maze = MazeGraph(height, width)
    maze = simplePrims(maze)
    for n in maze.nodes:
        n.printNode('\n')
    print_maze(maze)

if __name__ == '__main__':
    main()