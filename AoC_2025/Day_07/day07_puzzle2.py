import sys

def read_datas(input_file):
    # opening the file in read mode 
    my_file = open(input_file) 
    # reading the file 
    data = my_file.readlines()
    # store diagram, and add ghost boundaries
    tachyonManifold = []
    tachyonBeam = [0,0]
    for i in range(len(data)):
        line = data[i].strip()
        lineList = []
        for j in range(len(line)):
            lineList.append(line[j])
            if line[j] == 'S':
                tachyonBeam = [i,j]
        tachyonManifold.append(lineList)
    # closing file
    my_file.close()
    # return the lists
    return tachyonManifold, tachyonBeam

def goDown(tachyonManifold, tachyonBeam, tachyonBeamHeap):
    if tachyonBeam[0] < len(tachyonManifold):
        if tachyonBeam[1] >= 0 and tachyonBeam[1] < len(tachyonManifold[0]):
            if tachyonManifold[tachyonBeam[0]][tachyonBeam[1]] == '.':
                tachyonManifold[tachyonBeam[0]][tachyonBeam[1]] = '|'
                tachyonBeamHeap.append([tachyonBeam[0], tachyonBeam[1]])
    return tachyonManifold, tachyonBeamHeap

def splitBeam(tachyonManifold, tachyonBeam, tachyonBeamHeap):
    tachyonManifold, tachyonBeamHeap = goDown(tachyonManifold, [tachyonBeam[0]+1, tachyonBeam[1]-1], tachyonBeamHeap)
    tachyonManifold, tachyonBeamHeap = goDown(tachyonManifold, [tachyonBeam[0]+1, tachyonBeam[1]+1], tachyonBeamHeap)
    return tachyonManifold, tachyonBeamHeap

def advanceBeam(tachyonManifold, tachyonBeamHeap):
    tachyonBeam = tachyonBeamHeap.pop()
    if tachyonBeam[0] < len(tachyonManifold)-1 and tachyonManifold[tachyonBeam[0]+1][tachyonBeam[1]] == '.':
        tachyonManifold, tachyonBeamHeap = goDown(tachyonManifold, [tachyonBeam[0]+1, tachyonBeam[1]], tachyonBeamHeap)
    elif tachyonBeam[0] < len(tachyonManifold)-1 and tachyonManifold[tachyonBeam[0]+1][tachyonBeam[1]] == '^':
        tachyonManifold, tachyonBeamHeap = splitBeam(tachyonManifold, tachyonBeam, tachyonBeamHeap)
    return tachyonManifold, tachyonBeamHeap

def reformateTachyonManifold(tachyonManifold):
    for i in range(len(tachyonManifold)):
        for j in range(len(tachyonManifold[0])):
            if tachyonManifold[i][j] == 'S':
                tachyonManifold[i][j] = 1
            elif tachyonManifold[i][j] == '|':
                tachyonManifold[i][j] = 1
            elif tachyonManifold[i][j] == '.':
                tachyonManifold[i][j] = 0
            elif tachyonManifold[i][j] == '^':
                tachyonManifold[i][j] = -1
    return tachyonManifold

def computeBeamNbrTimelines(tachyonManifold, tachyonBeam):
    nbrTimelines = 0
    if tachyonBeam[0] > 0:
        nbrTimelines += tachyonManifold[tachyonBeam[0]-1][tachyonBeam[1]]
    if tachyonBeam[1] > 0 and tachyonManifold[tachyonBeam[0]][tachyonBeam[1]-1] == -1:
        nbrTimelines += tachyonManifold[tachyonBeam[0]-1][tachyonBeam[1]-1]
    if tachyonBeam[1] < len(tachyonManifold[0])-1 and tachyonManifold[tachyonBeam[0]][tachyonBeam[1]+1] == -1:
        nbrTimelines += tachyonManifold[tachyonBeam[0]-1][tachyonBeam[1]+1]
    return nbrTimelines

def computeTotalNbrTimelines(tachyonManifold):
    for i in range(1,len(tachyonManifold)):
        for j in range(len(tachyonManifold[0])):
            if tachyonManifold[i][j] == 1:
                tachyonManifold[i][j] = computeBeamNbrTimelines(tachyonManifold, [i,j])
    nbrTimelines = 0
    for j in range(len(tachyonManifold[0])):
        if tachyonManifold[-1][j] > 0:
            nbrTimelines += tachyonManifold[-1][j]
    return nbrTimelines

def solve(input_file):
    tachyonManifold, startBeam = read_datas(input_file)
    tachyonBeamHeap = [startBeam]
    while tachyonBeamHeap:
        tachyonManifold, tachyonBeamHeap = advanceBeam(tachyonManifold, tachyonBeamHeap)
    # we reformate the tachyonManifold grid to compute the number of timelines
    tachyonManifold = reformateTachyonManifold(tachyonManifold)
    nbrTimelines = computeTotalNbrTimelines(tachyonManifold)
    return nbrTimelines

# unit tests
tachyonManifold_test, tachyonBeam_test = read_datas("day07_data_test.txt")
assert(solve("day07_data_test.txt") == 40)

# print solution
if len(sys.argv) > 1:
    print("Number of timelines: ", solve(sys.argv[1]))