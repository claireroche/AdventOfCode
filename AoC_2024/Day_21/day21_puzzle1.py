def read_datas(input_file):
    # opening the file in read mode 
    my_file = open(input_file) 
    # read char by char
    datas = my_file.readlines()
    # fill the sequences
    sequences = []
    for line in datas:
        line = line.strip()
        sequences.append(line)
    # closing file
    my_file.close()
    # return the sequences
    return sequences

def buildNumericPad():
    pad = []
    pad.append(['7','8','9'])
    pad.append(['4','5','6'])
    pad.append(['1','2','3'])
    pad.append(['#','0','A'])
    padDic = {}
    for i in range(0,len(pad)):
        for j in range(0,len(pad[i])):
            padDic[pad[i][j]] = (i,j)
    return padDic

def buildDirPad():
    pad = []
    pad.append(['#','^','A'])
    pad.append(['<','v','>'])
    padDic = {}
    for i in range(0,len(pad)):
        for j in range(0,len(pad[i])):
            padDic[pad[i][j]] = (i,j)
    return padDic

def goFromTo(pad, num0, num1):
    pos0 = pad[num0]
    pos1 = pad[num1]
    i = pos1[0] - pos0[0]
    j = pos1[1] - pos0[1]
    return i, j

def getDirections(directions):
    dirChar = ''
    print(directions)
    for dir in directions:
        if dir[0] < 0:
            dirChar += abs(dir[0])*'^'
        elif dir[0] > 0:
            dirChar += abs(dir[0])*'v'
        if dir[1] < 0:
            dirChar += abs(dir[1])*'<'
        elif dir[1] > 0:
            dirChar += abs(dir[1])*'>'
        if dir == (0,0):
            dirChar += 'A'
    return dirChar
    

def buildDirOnNumPad(pad, sequence):
    # we start at position of 'A'
    directions = []
    previousNum = 'A'
    for num in sequence:
        i, j = goFromTo(pad, previousNum, num)
        previousNum = num
        directions.append((i,j))
        # add press buton instruction
        directions.append((0,0))
    return directions


# unit tests
sequences_test = read_datas("day21_data_test.txt")
print(sequences_test)
padNum_test = buildNumericPad()
padDir_test = buildDirPad()
sequence_2_test = getDirections(buildDirOnNumPad(padNum_test, '029A'))
print(sequence_2_test)
sequence_3_test = getDirections(buildDirOnNumPad(padDir_test, sequence_2_test))
print(sequence_3_test)
sequence_4_test = getDirections(buildDirOnNumPad(padDir_test, sequence_3_test))
print(sequence_4_test)