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

def advanceBeam(tachyonManifold, tachyonBeamHeap, sumSplit):
    tachyonBeam = tachyonBeamHeap.pop()
    if tachyonBeam[0] < len(tachyonManifold)-1 and tachyonManifold[tachyonBeam[0]+1][tachyonBeam[1]] == '.':
        tachyonManifold, tachyonBeamHeap = goDown(tachyonManifold, [tachyonBeam[0]+1, tachyonBeam[1]], tachyonBeamHeap)
    elif tachyonBeam[0] < len(tachyonManifold)-1 and tachyonManifold[tachyonBeam[0]+1][tachyonBeam[1]] == '^':
        tachyonManifold, tachyonBeamHeap = splitBeam(tachyonManifold, tachyonBeam, tachyonBeamHeap)
        sumSplit += 1
    return tachyonManifold, tachyonBeamHeap, sumSplit

def solve(input_file):
    tachyonManifold, tachyonBeam = read_datas(input_file)
    tachyonBeamHeap = [tachyonBeam]
    sumSplit = 0
    while tachyonBeamHeap:
        tachyonManifold, tachyonBeamHeap, sumSplit = advanceBeam(tachyonManifold, tachyonBeamHeap, sumSplit)
    for line in tachyonManifold:
        print(line)
    return sumSplit

# unit tests
tachyonManifold_test, tachyonBeam_test = read_datas("day07_data_test.txt")
assert(solve("day07_data_test.txt")==21)

# print solution
if len(sys.argv) > 1:
    print("Number of splits: ", solve(sys.argv[1]))