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

def evolveAllSN(sNs):
    newSNS = []
    for sN in sNs:
        newSN = sN
        for i in range(0,2000):
            newSN = evolveSN(newSN)
        newSNS.append(newSN)
    return newSNS

def solve(input_file):
    secretNumbers = read_datas(input_file)
    evolvedSNs = evolveAllSN(secretNumbers)
    sum = 0
    for i in range(0,len(secretNumbers)):
        sum += evolvedSNs[i]
    return sum


# unit tests
secretNumbers_test = read_datas("day22_data_test.txt")
print(secretNumbers_test)
assert(solve("day22_data_test.txt")==37327623)

# print result
print("Sum of new secret numbers:", solve("day22_data.txt"))