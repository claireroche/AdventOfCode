def read_datas(input_file):
    # opening the file in read mode 
    my_file = open(input_file) 
    # read line by line
    datas = my_file.readlines()
    # fill the links
    links = {}
    for line in datas:
        line = line.strip()
        computer1 =line[:2]
        computer2 = line[3:]
        if computer1 in links:
            links[computer1].append(computer2)
        else:
            links[computer1] = [computer2]
        if computer2 in links:
            links[computer2].append(computer1)
        else:
            links[computer2] = [computer1]
    # closing file
    my_file.close()
    # return the maze
    return links

def includeT(computersSet):
    for computer in computersSet:
        if computer[0] == 't':
            return True
    return False

def findThreeComputersSets(links):
    threeComputersSets = []
    for computer1 in links:
        for computer2 in links[computer1]:
            for computer3 in links[computer2]:
                set = sorted([computer1, computer2, computer3])
                if computer3 in links[computer1] and set not in threeComputersSets and includeT(set):
                    threeComputersSets.append(set)
    return threeComputersSets

def solve(input_file):
    # read datas
    links = read_datas(input_file)
    sets = findThreeComputersSets(links)
    return len(sets)

# unit tests
links_test = read_datas("day23_data_test.txt")
assert(solve("day23_data_test.txt")==7)

# print result
print("Number of sets of 3 interconnected computers with at least one T:", solve("day23_data.txt"))