import sys

def read_datas(input_file):
    # opening the file in read mode 
    my_file = open(input_file) 
    # read char by char
    datas = my_file.readlines()
    # fill the maze
    maze = []
    for line in datas:
        line = line.strip()
        l =[]
        for char in line:
            l.append(char)
        maze.append(l)
    # closing file
    my_file.close()
    # return the maze
    return maze

def getStart(maze):
    start = (0,0)
    for i in range(1,len(maze)-1):
        for j in range(1,len(maze[i])-1):
            if maze[i][j] == 'S':
                return (i,j)
    return start

def isNextCell(maze, path, cell, side):
    if maze[cell[0]+side[0]][cell[1]+side[1]] != '#' and (cell[0]+side[0],cell[1]+side[1]) not in path:
        return True
    return False

def findNextCell(maze, path, cell):
    side = (0,0)
    if isNextCell(maze, path, cell, (-1, 0)):
        side = (-1,0)
    if isNextCell(maze, path, cell, (1,0)):
        side = (1,0)
    if isNextCell(maze, path, cell, (0,-1)):
        side = (0,-1)
    if isNextCell(maze, path, cell, (0,1)):
        side = (0,1)
    return (cell[0]+side[0],cell[1]+side[1])

def findPath(maze):
    start = getStart(maze)
    path = [start]
    while maze[path[-1][0]][path[-1][1]] != 'E':
        path.append(findNextCell(maze, path, path[-1]))
    return path

def getGridDistance(cell0, cell1):
    return abs(cell0[0]-cell1[0]) + abs(cell0[1]-cell1[1]) +1

def save100Picoseconds(maze, path, cell0, cell1):
    dist = getGridDistance(cell0, cell1)
    if dist-1 > 20 or dist < 3:
        return False
    tmp_len = len(path[0:path.index(cell0)+1])-1 + len(path[path.index(cell1):])-1 + dist-1
    if len(path)-1 - (tmp_len-1) >= 100:
        return True
    return False

def getNbrShortcutsFromCell(maze, path, cell):
    nbrShortcuts = 0
    index_cell = path.index(cell)
    for i in range(index_cell+1,len(path)):
        if save100Picoseconds(maze, path, cell, path[i]):
            nbrShortcuts += 1
    return nbrShortcuts

def solve(input_file):
    # read input datas
    maze = read_datas(input_file)
    # compute the path
    path = findPath(maze)
    # 
    nbrShortcuts = 0
    for i in range(0,len(path)):
        nbrShortcuts += getNbrShortcutsFromCell(maze, path, path[i])
    return nbrShortcuts

# unit test
maze_test = read_datas("day20_data_test.txt")
start_test = getStart(maze_test)
assert(start_test==(3,1))
path_test = findPath(maze_test)
assert(len(path_test)-1==84)
assert(getGridDistance((0,0), (1,1))==3)

# solve puzzle
print(solve("day20_data.txt"))