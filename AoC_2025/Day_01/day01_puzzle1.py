import sys

def read_datas(input_file):
    # open file
    my_file = open(input_file)
    # read lines
    data = my_file.readlines()
    # create rotations list
    rotations = []
    for line in data:
        # add rotation
        rotations.append([line[0], int(line[1:])])
    # closing file
    my_file.close()

    return rotations

def rotate(dial, rotation):
    if rotation[0] == 'L':
        side = -1
    else:
        side = 1
    return (dial + side*rotation[1])%100

def solve(input_data):
    rotations = read_datas(input_data)
    dial = 50
    counter = 0
    for rotation in rotations:
        dial = rotate(dial, rotation)
        if dial == 0:
            counter += 1
    return counter


# unit tests
rotations = read_datas("day01_data_test.txt")
assert(rotations[0] == ['L',68])
assert(rotate(50, ['L',68]) == 82)
assert(solve("day01_data_test.txt") == 3)

# plot solution
if len(sys.argv) > 1:
    print("Password to open the door: ", solve(sys.argv[1]))