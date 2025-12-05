import re

def read_datas(input_file):
    # opening the file in read mode 
    my_file = open(input_file) 
    # read line by line
    datas = my_file.readlines()
    # fill 
    gates = {}
    wiresXOR = []
    wiresOR = []
    wiresAND = []
    for line in datas:
        line = line.strip()
        if len(line) < 7 and len(line) > 1:
            #print(line)
            line = line.split(': ')
            gates[line[0]] = int(line[1])
        elif len(line) > 7:
            wire = []
            line = line.split(' -> ')
            wire.append(line[0][0:3])
            if re.findall(r' XOR ', line[0]):
                wire.append(line[0][8:11])
                wiresXOR.append(wire + [line[1]])
            if re.findall(r' OR ', line[0]):
                wire.append(line[0][7:10])
                wiresOR.append(wire+[line[1]])
            if re.findall(r' AND ', line[0]):
                wire.append(line[0][8:11])
                wiresAND.append(wire+[line[1]])
    # closing file
    my_file.close()
    # return the gates and wires to compute
    return gates, wiresOR, wiresAND, wiresXOR

def computeORwire(gates, wire):
    return gates[wire[0]] or gates[wire[1]]

def computeANDwire(gates, wire):
    return gates[wire[0]] and gates[wire[1]]

def computeXORwire(gates, wire):
    return gates[wire[0]] ^ gates[wire[1]]

def computeORwires(gates, wiresOR):
    for wire in wiresOR:
        if wire[0] in gates and wire[1] in gates:
            wiresOR.remove(wire)
            gates[wire[2]] = computeORwire(gates, wire)
    return gates, wiresOR

def computeANDwires(gates, wiresAND):
    for wire in wiresAND:
        if wire[0] in gates and wire[1] in gates:
            wiresAND.remove(wire)
            gates[wire[2]] = computeANDwire(gates, wire)
    return gates, wiresAND

def computeXORwires(gates, wiresXOR):
    for wire in wiresXOR:
        if wire[0] in gates and wire[1] in gates:
            wiresXOR.remove(wire)
            gates[wire[2]] = computeXORwire(gates, wire)
    return gates, wiresXOR

def computeWires(gates, wiresOR, wiresAND, wiresXOR):
    while len(wiresOR) > 0 or len(wiresAND) > 0 or len(wiresXOR) > 0:
        if len(wiresOR) > 0:
            gates, wiresOR = computeORwires(gates, wiresOR)
        if len(wiresAND) > 0:
            gates, wiresAND = computeANDwires(gates, wiresAND)
        if len(wiresXOR) > 0:
            gates, wiresXOR = computeXORwires(gates, wiresXOR)
    return gates

def orderZGates(gates):
    zgates = []
    for gate in gates:
        if gate[0] == 'z':
            zgates.append(gate)
    zgates.sort()
    return reversed(zgates)

def buildBinZGates(gates, zgates):
    binZgates = ''
    for gate in zgates:
        binZgates += str(gates[gate])
    return binZgates

def solve(input_file):
    # read datas
    gates, wiresOR, wiresAND, wiresXOR = read_datas(input_file)
    # 
    gates = computeWires(gates, wiresOR, wiresAND, wiresXOR)
    #
    zgates = orderZGates(gates)
    # build the corresponding binary repr
    binZGates = buildBinZGates(gates, zgates)
    return int(binZGates, 2)

# unit tests
gates_test, wiresOR_test, wiresAND_test, wiresXOR_test = read_datas("day24_data_test.txt")
gates_test = computeWires(gates_test, wiresOR_test, wiresAND_test, wiresXOR_test)
zgates = orderZGates(gates_test)
assert(solve("day24_data_test.txt")==2024)

# print solution
print("Decimal number output on the wires starting with Z:", solve("day24_data.txt"))