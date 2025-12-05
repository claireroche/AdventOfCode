import sys

def read_datas(input_file):
    # opening the file in read mode 
    my_file = open(input_file) 
    # reading the file 
    data = my_file.readlines()
    # init the ranges and ingredients
    ranges = []
    for line in data:
        line = line.strip()
        if (line.count('-')):
            line = line.split('-')
            range = []
            range.append(int(line[0]))
            range.append(int(line[1]))
            ranges.append(range)
    # closing file
    my_file.close()
    # return the lists
    return ranges

def concatenateTwoRanges(ranges, r1, r2):
    # we assume in this function that r1[0] <= r2[0]
    changed = False
    if r1[1] >= r2[0]:
        r3 = [r1[0], max(r1[1], r2[1])]
        ranges.remove(r1)
        ranges.remove(r2)
        ranges.append(r3)
        changed = True
    return ranges, changed

def concatenateRanges(ranges):
    changed = False
    i = 0
    while not changed and i < len(ranges):
        j = 0
        while not changed and j < len(ranges):
            if i != j and ranges[i][0] <= ranges[j][0]:
                ranges, changed = concatenateTwoRanges(ranges, ranges[i], ranges[j])
            elif i != j and ranges[j][0] <= ranges[i][0]:
                ranges, changed = concatenateTwoRanges(ranges, ranges[j], ranges[i])
            j += 1
        i += 1
    return ranges, changed

def iterativeConcatenate(ranges):
    changed = True
    while changed:
        ranges, changed = concatenateRanges(ranges)
    return ranges

def solve(input_file):
    ranges = read_datas(input_file)
    ranges = iterativeConcatenate(ranges)
    nbrFreshIngredients = 0
    for r in ranges:
        nbrFreshIngredients += r[1]-r[0]+1
    return nbrFreshIngredients


# unit tests
ranges_test = read_datas("day05_data_test.txt")
assert(len(iterativeConcatenate(ranges_test)) == 2)
assert(solve("day05_data_test.txt") == 14)


# print solution
if len(sys.argv) > 1:
    print("Number of fresh ingredient IDs: ", solve(sys.argv[1]))