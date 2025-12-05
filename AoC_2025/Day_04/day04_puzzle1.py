import sys

def read_datas(input_file):
    # opening the file in read mode 
    my_file = open(input_file) 
    # reading the file 
    data = my_file.readlines()
    # store diagram, and add ghost boundaries
    diagram = []
    firstLine = '#'*(len(data[0].strip())+2)
    diagram.append(firstLine)
    for line in data:
        line = '#' + line.strip() + '#'
        diagram.append(line)
    diagram.append(firstLine)
    # closing file
    my_file.close()
    # return the lists
    return diagram

def addRoll(diagram, i, j):
    nbrRoll = 0
    if diagram[i][j] == '@':
        nbrRoll = 1
    return nbrRoll

def isAccessible(diagram, i, j):
    isAccess = False
    counterRolls = 0
    counterRolls += addRoll(diagram, i-1, j-1)
    counterRolls += addRoll(diagram, i-1, j  )
    counterRolls += addRoll(diagram, i-1, j+1)
    counterRolls += addRoll(diagram,   i, j-1)
    counterRolls += addRoll(diagram,   i, j+1)
    counterRolls += addRoll(diagram, i+1, j-1)
    counterRolls += addRoll(diagram, i+1, j  )
    counterRolls += addRoll(diagram, i+1, j+1)
    
    if counterRolls < 4:
        isAccess = True
    return isAccess

def solve(input_file):
    countAccessibleRolls = 0
    diagram = read_datas(input_file)
    for i in range(1,len(diagram)-1):
        for j in range(1,len(diagram[0])-1):
            # if it's a roll, we check if it's accessible
            if diagram[i][j] == '@' and isAccessible(diagram, i, j):
                countAccessibleRolls += 1
    return countAccessibleRolls

# unit tests
diagram_test = read_datas("day04_data_test.txt")
assert(len(diagram_test[0]) == len(diagram_test[1]))
assert(solve("day04_data_test.txt") == 13)

# print solution
if len(sys.argv) > 1:
    print("Number of rolls accessible: ", solve(sys.argv[1]))