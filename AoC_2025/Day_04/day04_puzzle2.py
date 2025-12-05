import sys

def read_datas(input_file):
    # opening the file in read mode 
    my_file = open(input_file) 
    # reading the file 
    data = my_file.readlines()
    # store diagram, and add ghost boundaries
    diagram = []
    firstLine = ['#']*(len(data[0].strip())+2)
    diagram.append(firstLine)
    for line in data:
        line = line.strip()
        lineDiagram = ['#']
        for pos in line:
            lineDiagram.append(pos)
        lineDiagram.append('#')
        diagram.append(lineDiagram)
    diagram.append(firstLine)
    # closing file
    my_file.close()
    # return the lists
    return diagram

def initRollsHeap(diagram):
    """
    Takes the diagram of rolls as an input,
    and return a list of rolls positions.
    We will use this list as a heap.
    """
    rollsHeap = []
    for i in range(1,len(diagram)-1):
        for j in range(1,len(diagram[0])-1):
            if diagram[i][j] == '@':
                rollsHeap.append([i,j])
    return rollsHeap

def addRoll(diagram, i, j, adjRolls):
    if diagram[i][j] == '@':
        adjRolls.append([i,j])
    return adjRolls

def isAccessible(diagram, i, j):
    isAccess = False
    adjacentRolls = []
    adjacentRolls = addRoll(diagram, i-1, j-1, adjacentRolls)
    adjacentRolls = addRoll(diagram, i-1, j  , adjacentRolls)
    adjacentRolls = addRoll(diagram, i-1, j+1, adjacentRolls)
    adjacentRolls = addRoll(diagram,   i, j-1, adjacentRolls)
    adjacentRolls = addRoll(diagram,   i, j+1, adjacentRolls)
    adjacentRolls = addRoll(diagram, i+1, j-1, adjacentRolls)
    adjacentRolls = addRoll(diagram, i+1, j  , adjacentRolls)
    adjacentRolls = addRoll(diagram, i+1, j+1, adjacentRolls)
    if len(adjacentRolls) < 4:
        isAccess = True
    return isAccess, adjacentRolls

def updateDiagram(diagram, i, j):
    # remove the roll [i,j]
    diagram[i][j] = '.'
    return diagram

def updateRollsHeap(diagram, i, j, rollsHeap, adjacentRolls):
    # we add the adjacent rolls to the heap list of rolls to check
    for pos in adjacentRolls:
        if not pos in rollsHeap:
            rollsHeap.append(pos)
    return rollsHeap

def solve(input_file):
    countAccessibleRolls = 0
    diagram = read_datas(input_file)
    rollsHeap = initRollsHeap(diagram)
    # while there are rolls to check in the heap...
    while rollsHeap:
        roll = rollsHeap.pop()
        isAccess, adjacentRolls = isAccessible(diagram, roll[0], roll[1])
        if isAccess:
            countAccessibleRolls += 1
            # update diagram and rolls
            diagram = updateDiagram(diagram, roll[0], roll[1])
            rollsHeap = updateRollsHeap(diagram, roll[0], roll[1], rollsHeap, adjacentRolls)
    return countAccessibleRolls

# unit tests
diagram_test = read_datas("day04_data_test.txt")
assert(len(diagram_test[0]) == len(diagram_test[1]))
assert(solve("day04_data_test.txt") == 43)

# print solution
if len(sys.argv) > 1:
    print("Number of rolls accessible: ", solve(sys.argv[1]))