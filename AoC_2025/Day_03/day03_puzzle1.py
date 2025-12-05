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

def findLargestJoltage(bank):
    indexMaxFirst = 0
    i = 1
    while i < len(bank)-1 and bank[indexMaxFirst] != 9:
        if bank[i] > bank[indexMaxFirst]:
            indexMaxFirst = i
        i += 1

    indexMaxSecond = indexMaxFirst + 1
    j = indexMaxSecond + 1
    while j < len(bank) and bank[indexMaxSecond] != 9:
        if bank[j] > bank[indexMaxSecond]:
            indexMaxSecond = j
        j += 1

    return bank[indexMaxFirst]*10+bank[indexMaxSecond]

def solve(input_file):
    banks = read_datas(input_file)
    sumJoltage = 0
    for bank in banks:
        sumJoltage += findLargestJoltage(bank)
    return sumJoltage


# unit tests
banks_test = read_datas("day03_data_test.txt")
assert(len(banks_test) == 4)
assert(findLargestJoltage(banks_test[0]) == 98)
assert(findLargestJoltage(banks_test[1]) == 89)
assert(findLargestJoltage(banks_test[2]) == 78)
assert(findLargestJoltage(banks_test[3]) == 92)
assert(solve("day03_data_test.txt") == 357)

# print solution
if len(sys.argv) > 1:
    print("Password to open the door: ", solve(sys.argv[1]))