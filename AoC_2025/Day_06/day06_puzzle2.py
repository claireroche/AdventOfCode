import sys

def getRangeProblem(signsLine, indexStart):
    indexEnd = indexStart + 1
    while indexEnd < len(signsLine)-1 and signsLine[indexEnd+1] == ' ':
        indexEnd += 1
    return indexEnd

def getProblem(data, indexStart, indexEnd):
    # here, we must add a special case for the last problem
    # of the data-set, which is not made of a last ghost column
    # of spaces. We must add one to the index, otherwise, one
    # number will miss in the problem.
    if indexEnd == len(data[-1])-1:
        indexEnd += 1
    problem = []
    for i in range(indexStart, indexEnd):
        nbrChar = ''
        for j in range(len(data)-1):
            nbrChar += data[j][i]
        problem.append(int(nbrChar))
    return problem

def read_datas(input_file):
    # opening the file in read mode 
    my_file = open(input_file) 
    # reading the file 
    data = my_file.readlines()
    # we know that the signs are given by the last line of the input datas
    signsLine = data[-1]
    problemsList = []
    indexStart = -1
    indexEnd = -1
    while indexEnd < len(signsLine)-1:
        indexStart = indexEnd + 1
        indexEnd = getRangeProblem(signsLine, indexStart)
        problem = getProblem(data, indexStart, indexEnd)
        problemsList.append(problem)
    # read the signs list for the problems
    signsList = []
    line = signsLine.split()
    for sign in line:
        signsList.append(sign)
    # closing file
    my_file.close()
    # return the lists
    return problemsList, signsList

def solveProblemAdd(problem):
    sum = 0
    for nbr in problem:
        sum += nbr
    return sum

def solveProblemMult(problem):
    result = 1
    for nbr in problem:
        result *= nbr
    return result

def computeGrandTotal(problemsList, signsList):
    grandTotal = 0
    for i in range(len(problemsList)):
        if signsList[i] == '+':
            grandTotal += solveProblemAdd(problemsList[i])
        elif signsList[i] == '*':
            grandTotal += solveProblemMult(problemsList[i])
    return grandTotal

def solve(input_file):
    problemsList, signsList = read_datas(input_file)
    return computeGrandTotal(problemsList, signsList)

# unit tests
problemsList_test, signsList_test = read_datas("day06_data_test.txt")
assert(len(problemsList_test) == 4)
assert(len(problemsList_test[0]) == 3)
assert(len(problemsList_test[3]) == 3)
assert(len(signsList_test) == 4)
assert(solveProblemMult(problemsList_test[0]) == 8544)
assert(solveProblemAdd(problemsList_test[1]) == 625)
assert(solveProblemMult(problemsList_test[2]) == 3253600)
assert(solveProblemAdd(problemsList_test[3]) == 1058)
assert(signsList_test[0] == '*')
assert(signsList_test[3] == '+')
assert(solve("day06_data_test.txt") == 3263827)

# print solution
if len(sys.argv) > 1:
    print("Grand Total: ", solve(sys.argv[1]))