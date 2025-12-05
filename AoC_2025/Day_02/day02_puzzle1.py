import sys

def read_datas(input_file):
    # opening the file in read mode 
    my_file = open(input_file) 
    # reading the file 
    data = my_file.read()
    # split by ranges
    dataRanges = data.split(',')
    # store each ranges
    ranges = []
    for range in dataRanges:
        dataRange = range.split('-')
        ranges.append([dataRange[0], dataRange[1]])
    # closing file
    my_file.close()
    # return the lists
    return ranges

def sumInvalidIDsinRange(r):
    sum = 0
    for nbr in range(int(r[0]),int(r[1])+1):
        nbrChar = str(nbr)
        if len(nbrChar)%2 == 0:
            if nbrChar[0:len(nbrChar)//2] == nbrChar[len(nbrChar)//2:]:
                sum += nbr
    return sum

def solve(input_file):
    ranges = read_datas(input_file)
    sumTotal = 0
    for range in ranges:
        sumTotal += sumInvalidIDsinRange(range)
    return sumTotal

# unit tests
ranges_test = read_datas("day02_data_test.txt")
assert(sumInvalidIDsinRange(ranges_test[0])==33)
assert(solve("day02_data_test.txt") == 1227775554)

# print solution
if len(sys.argv) > 1:
    print("Password to open the door: ", solve(sys.argv[1]))