import sys

def read_datas(input_file):
    # opening the file in read mode 
    my_file = open(input_file) 
    # reading the file 
    data = my_file.readlines()
    # init problems list
    lineInit = data[0].strip().split()
    problemsList = [[] for i in range(len(lineInit))]
    for indexLine in range(len(data)-1):
        line = data[indexLine].strip().split()
        for indexNbr in range(len(line)):
            problemsList[indexNbr].append(int(line[indexNbr]))
    # read the signs list for the problems
    signsList = []
    line = data[-1].strip().split()
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
assert(len(signsList_test) == 4)
assert(problemsList_test[0][1] == 45)
assert(problemsList_test[1][0] == 328)
assert(problemsList_test[3][2] == 314)
assert(signsList_test[0] == '*')
assert(signsList_test[3] == '+')
assert(computeGrandTotal(problemsList_test, signsList_test) == 4277556)
assert(solve("day06_data_test.txt") == 4277556)

# print solution
if len(sys.argv) > 1:
    print("Grand Total: ", solve(sys.argv[1]))