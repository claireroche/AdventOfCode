import sys

def read_datas(input_file):
    # opening the file in read mode 
    my_file = open(input_file) 
    # reading the file 
    data = my_file.readlines()
    # store each bank
    banks = []
    for line in data:
        line = line.strip()
        bank = []
        for battery in line:
            bank.append(int(battery))
        banks.append(bank)
    # closing file
    my_file.close()
    # return the lists
    return banks

def findIthIndex(bank, i, previousPickedIndex):
    indexMax = previousPickedIndex + 1
    j = indexMax + 1
    while j < len(bank)-(12-i) and bank[indexMax] != 9:
        if bank[j] > bank[indexMax]:
            indexMax = j
        j += 1
    return indexMax

def findLargestJoltageIndices(bank):
    indicesMax = [-1]*12
    for i in range(1,13):
        if i == 1:
            previousPickedIndex = -1
        else:
            previousPickedIndex = indicesMax[i-2]
        indicesMax[i-1] = findIthIndex(bank, i, previousPickedIndex)
    return indicesMax

def getLargestJoltage(bank, indices):
    joltage = ''
    for index in indices:
        joltage += str(bank[index])
    return int(joltage)

def solve(input_file):
    banks = read_datas(input_file)
    sumJoltage = 0
    for bank in banks:
        maxIndices = findLargestJoltageIndices(bank)
        sumJoltage += getLargestJoltage(bank, maxIndices)
    return sumJoltage


# unit tests
banks_test = read_datas("day03_data_test.txt")
assert(len(banks_test) == 4)
assert(solve("day03_data_test.txt") == 3121910778619)

# print solution
if len(sys.argv) > 1:
    print("Password to open the door: ", solve(sys.argv[1]))