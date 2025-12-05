import sys

def read_datas(input_file):
    # opening the file in read mode 
    my_file = open(input_file) 
    # reading the file 
    data = my_file.readlines()
    # init the ranges and ingredients
    ranges = []
    ingredients = []
    for line in data:
        line = line.strip()
        if (line.count('-')):
            line = line.split('-')
            range = []
            range.append(int(line[0]))
            range.append(int(line[1]))
            ranges.append(range)
        elif (len(line)):
            line = line.strip()
            ingredients.append(int(line))
    # closing file
    my_file.close()
    # return the lists
    return ranges, ingredients

def isFresh(ranges, ingredient):
    fresh = False
    indexRanges = 0
    while not fresh and indexRanges < len(ranges):
        if ranges[indexRanges][0] <= ingredient and ingredient <= ranges[indexRanges][1]:
            fresh = True
        indexRanges += 1
    return fresh

def solve(input_file):
    ranges, ingredients = read_datas(input_file)
    countFreshIngredients = 0
    for ingredient in ingredients:
        if isFresh(ranges, ingredient):
            countFreshIngredients += 1
    return countFreshIngredients


# unit tests
ranges_test, ingredients_test = read_datas("day05_data_test.txt")
assert(solve("day05_data_test.txt") == 3)

# print solution
if len(sys.argv) > 1:
    print("Number of fresh ingredient IDs: ", solve(sys.argv[1]))