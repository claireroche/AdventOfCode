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

def isOut(maze, cell):
    return cell[0] < 0 or cell[1] < 0 or cell[0] > len(maze) or cell[1] > len(maze[cell[0]])

def getStart(maze):
    start = (0,0)
    for i in range(1,len(maze)-1):
        for j in range(1,len(maze[i])-1):
            if maze[i][j] == 'S':
                return (i,j)
    return start

def getEnd(maze):
    end = (0,0)
    for i in range(1,len(maze)-1):
        for j in range(1,len(maze[i])-1):
            if maze[i][j] == 'E':
                return (i,j)
    return end

def initDistancesMap(grid, start):
    distMap = {}
    freeCells = []
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            if grid[i][j] !='#':
                distMap[(i,j)] = sys.maxsize
                freeCells.append((i,j))
    distMap[start] = 0
    return distMap, freeCells

def updateAdjDistances(distMap, pos1, pos2, previousPos):
    if pos2 in distMap and distMap[pos2] > distMap[pos1] + 1:
            distMap[pos2] = distMap[pos1] + 1
            # update states
            previousPos[pos2] = pos1
    return distMap

def getMinElement(freeCells, distMap):
    cell = freeCells[0]
    minDist = distMap[cell]
    for i in range(1,len(freeCells)):
        if minDist > distMap[freeCells[i]]:
            cell = freeCells[i]
            minDist = distMap[cell]
    return cell

def buildPath(previousPos, start, end):
    cell = end
    path = []
    while cell != start:
        path += [cell]
        cell = previousPos[cell]
    path += [start]
    return path

def printMaze(grid, path):
    for i in range(0,len(grid)):
        char = ''
        for j in range(0,len(grid[i])):
            if (i,j) in path:
                char += '0'
            else:
                char += grid[i][j]
        print(char)

def getPath(maze, start, end):
    # init distance map, and non-visited cells heap
    distMap, freeCells = initDistancesMap(maze, start)
    # init previous positions map
    previousPos = {}
    while len(freeCells) > 0:
        # get min position
        pos = getMinElement(freeCells, distMap)
        # remove from heap
        freeCells.pop(freeCells.index(pos))
        # update distance map
        distMap = updateAdjDistances(distMap, pos, (pos[0]+1, pos[1]  ), previousPos)
        distMap = updateAdjDistances(distMap, pos, (pos[0]-1, pos[1]  ), previousPos)
        distMap = updateAdjDistances(distMap, pos, (pos[0]  , pos[1]+1), previousPos)
        distMap = updateAdjDistances(distMap, pos, (pos[0]  , pos[1]-1), previousPos)
    # build the path
    path = buildPath(previousPos, start, end)
    return path

def newPathLenght(maze, path, cell0, cell1, end):
    tmp_len = len(path[0:path.index(cell0)+1]) + len(path[path.index(cell1):]) +1
    return tmp_len

def save100Picoseconds(maze, path, cell, side, end):
    index_cell = path.index(cell)
    if maze[cell[0]+side[0]][cell[1]+side[1]] == '#' and (cell[0]+2*side[0], cell[1]+2*side[1]) in path:
        if index_cell < path.index((cell[0]+2*side[0], cell[1]+2*side[1])):
            tmp_len = newPathLenght(maze, path, cell, (cell[0]+2*side[0], cell[1]+2*side[1]), end)
            if len(path)-1 - (tmp_len-1) >= 100:
                return True
    return False

def getNbrShortcutsFromCell(maze, path, cell, end):
    nbrShortcuts = 0
    if save100Picoseconds(maze, path, cell, (-1,0), end):
        nbrShortcuts += 1
    if save100Picoseconds(maze, path, cell, (1,0), end):
        nbrShortcuts += 1
    if save100Picoseconds(maze, path, cell, (0,-1), end):
        nbrShortcuts += 1
    if save100Picoseconds(maze, path, cell, (0,1), end):
        nbrShortcuts += 1
    return nbrShortcuts

def solve(input_file):
    # read input datas
    maze = read_datas(input_file)
    # get start and end positions
    start = getStart(maze)
    end = getEnd(maze)
    # compute the path
    path = getPath(maze, start, end)
    # 
    nbrShortcuts = 0
    for i in range(0,len(path)-99):
        print("cell", path[i])
        nbrShortcuts += getNbrShortcutsFromCell(maze, path, path[i], end)

    return nbrShortcuts

# unit test
maze_test = read_datas("day20_data_test.txt")
start_test = getStart(maze_test)
end_test = getEnd(maze_test)
assert(start_test==(3,1))
assert(end_test==(7,5))
path_test = getPath(maze_test, start_test, end_test)
assert(len(path_test)-1==84)
print(maze_test)

# solve puzzle
print(solve("day20_data.txt"))