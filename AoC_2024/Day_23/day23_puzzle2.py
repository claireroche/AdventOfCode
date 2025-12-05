def read_datas(input_file):
    # opening the file in read mode 
    my_file = open(input_file) 
    # read line by line
    datas = my_file.readlines()
    # fill the links
    links = {}
    for line in datas:
        line = line.strip()
        computers = sorted([line[:2], line[3:]])
        if computers[0] in links:
            links[computers[0]].append(computers[1])
        else:
            links[computers[0]] = [computers[1]]
    # closing file
    my_file.close()
    # return the maze
    return links

def findThreeComputersSets(links):
    threeComputersSets = []
    for computer1 in links:
        for computer2 in links[computer1]:
            for computer3 in links[computer2]:
                set = sorted([computer1, computer2, computer3])
                if computer3 in links[computer1] and set not in threeComputersSets:
                    threeComputersSets.append(set)
    return threeComputersSets

def findLongestInterconnectedSet(links, computer):
    set = []
    heap = []
    # init heap
    for computer2 in links[computer]:
        heap.append([computer, computer2])
    # compute longest set starting from computer
    while len(heap) > 0:
        locSet = heap.pop()
        if locSet[-1] in links:
            for computerNext in links[locSet[-1]]:
                isConnected = True
                i = 0
                while isConnected and i < len(locSet):
                    if computerNext not in links[locSet[i]]:
                        isConnected = False
                    i += 1
                if isConnected:
                    heap.append(locSet + [computerNext])
                    if len(locSet + [computerNext]) > len(set):
                        set = locSet + [computerNext]
    return set

def convertToChar(set):
    setChar = str(set[0])
    for i in range(1,len(set)):
        setChar += ',' + str(set[i])
    return setChar

def solve(input_file):
    # read datas
    links = read_datas(input_file)
    set = []
    for computer in links:
        locSet = findLongestInterconnectedSet(links, computer)
        if len(locSet) > len(set):
            set = locSet
    return convertToChar(sorted(set))

# unit tests
links_test = read_datas("day23_data_test.txt")
assert(solve("day23_data_test.txt")=='co,de,ka,ta')

# print result
print("Longest interconnected set:", solve("day23_data.txt"))