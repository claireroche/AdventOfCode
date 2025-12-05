def read_datas(input_file):
    # opening the file in read mode 
    my_file = open(input_file) 
    # read line by line
    datas = my_file.readlines()
    # fill the secret numbers
    secretNumbers = []
    for line in datas:
        secretNumbers.append(int(line))
    # closing file
    my_file.close()
    # return the secret numbers
    return secretNumbers

def mix(sN, value):
    return sN^value

def prune(sN):
    return sN%16777216

def evolveSN(sN):
    newSN = sN
    # step 1:
    newSN = mix(sN, sN*64)
    newSN = prune(newSN)
    # step 2:
    newSN = mix(newSN, int(newSN/32))
    newSN = prune(newSN)
    # step 3:
    newSN = mix(newSN, newSN*2048)
    newSN = prune(newSN)
    # return evolved secret number
    return newSN

def evolveSNMTimes(sN, times):
    priceSN = [int(str(sN)[-1])]
    newSN = sN
    for i in range(0,times):
        newSN = evolveSN(newSN)
        priceSN.append(int(str(newSN)[-1]))
    return newSN, priceSN

def evolveAllSN(sNs):
    newSNS = []
    pricesTables = []
    for sN in sNs:
        newSN, priceSN = evolveSNMTimes(sN, 2000)
        newSNS.append(newSN)
        pricesTables.append(priceSN)
    return newSNS, pricesTables

def buildSequence(priceTable, index):
    sequence = []
    for i in range(index,index+4):
        sequence.append(priceTable[i]-priceTable[i-1])
    return sequence

def computeSequencesGain(pricesTables):
    globalSequencesGain = []
    globalSequencesList = []

    # build list of existing sequences
    for priceTable in pricesTables:
        print("Secret Number:", pricesTables.index(priceTable))
        sequencesListLoc = []
        for i in range(1, len(priceTable)-3):
            sequence = buildSequence(priceTable, i)
            if sequence not in sequencesListLoc:
                sequencesListLoc.append(sequence)
                if sequence in globalSequencesList:
                    index = globalSequencesList.index(sequence)
                    globalSequencesGain[index] += priceTable[i+3]
                else:
                    globalSequencesList.append(sequence)
                    globalSequencesGain.append(priceTable[i+3])
    return globalSequencesGain, globalSequencesList

def getMaxGainSequence(sequencesGain, sequencesList):
    sequence = sequencesList[0]
    gain = sequencesGain[0]
    for i in range(1, len(sequencesGain)):
        if sequencesGain[i] > gain:
            sequence = sequencesList[i]
            gain = sequencesGain[i]
    return sequence, gain

def solve(input_file):
    secretNumbers = read_datas(input_file)
    finalSecretNumbers, pricesTables = evolveAllSN(secretNumbers)
    sequencesGain, sequencesList = computeSequencesGain(pricesTables)
    sequence, gain = getMaxGainSequence(sequencesGain, sequencesList)
    return gain


# unit tests
secretNumbers_test = read_datas("day22_data_test.txt")
print(secretNumbers_test)
finalSecretNumbers_test, pricesTables_test = evolveAllSN(secretNumbers_test)
#print(finalSecretNumbers_test)
#print(pricesTables_test)
#print(computeSequencesGain(pricesTables_test))
print(solve("day22_data_test2.txt")==23)
#assert(solve("day22_data_test.txt")==37327623)

# print result
print("Most bananas we can get:", solve("day22_data.txt"))