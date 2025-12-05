def read_datas(input_file):
    # opening the file in read mode 
    my_file = open(input_file) 
    # reading the file 
    data = my_file.readlines()
    # separate the two columns
    map = []
    for line in data:
        line = line.strip()
        line_list = []
        for char in line:
            line_list.append(char)
        map.append(line_list)
    # closing file
    my_file.close()
    # return the lists
    return map

class Map:
    def __init__(self, grid):
        self.grid = grid

    def isOut(self, i, j):
        return (i>len(self.grid) or j > len(self.grid[i]))
    
    def isObstruction(self, i, j):
        return (not self.isOut(i,j) and self.grid[i][j] == '#')

class Position:
    def __init__(self, coord_i, coord_j, side):
        self.coord_i = coord_i
        self.coord_j = coord_j
        self.side = side
    def __str__(self):
        return f"Coord i: {self.coord_i} \nCoord j: {self.coord_j} \nSide: {self.side}"

class Guard:
    def __init__(self, map):
        self.map = map
        for i in range(0,len(map.grid)):
            for j in range(0,len(map.grid[i])):
                if (map.grid[i][j] == '^' or map.grid[i][j] == '>' or map.grid[i][j] == 'v' or map.grid[i][j] == '<'):
                    self.position = Position(i, j, map.grid[i][j])

    def turnRight(self):
        if (self.position.side == '^'):
            self.position.side = '>'
        elif (self.position.side == '>'):
            self.position.side = 'v'
        elif (self.position.side == 'v'):
            self.position.side = '<'
        elif (self.position.side == '<'):
            self.position.side = '^'
        else:
            print("turnRight: unknown starting side.")
    
    def move(self):
        tmp_pos = self.position
        if (self.position.side == '^'):
            tmp_pos = Position(self.position.coord_i-1, self.position.coord_j, self.position.side)
        elif (self.position.side == '>'):
            tmp_pos = Position(self.position.coord_i, self.position.coord_j+1, self.position.side)
        elif (self.position.side == 'v'):
            tmp_pos = Position(self.position.coord_i+1, self.position.coord_j, self.position.side)
        elif (self.position.side == '<'):
            tmp_pos = Position(self.position.coord_i, self.position.coord_j-1, self.position.side)
        else:
            print("move: unknown side.")
        if (not self.map.isObstruction(tmp_pos.coord_i, tmp_pos.coord_j)):
            return tmp_pos
        else:
            return self.turnRight()

def solve(input_file):
    # read input datas
    grid = read_datas(input_file)
    # get init position of guard in the grid
    guard = Guard(map)
    # store the map
    map = Map(read_datas(input_file))

    sum = 0
    return sum


# unit tests
print(read_datas("day06_data_test.txt"))
map = Map(read_datas("day06_data_test.txt"))
assert(map.isOut(0,1)==False)
assert(map.isOut(101,3)==True)
assert(map.isObstruction(3,3)==False)
assert(map.isObstruction(3,2)==True)
guard = Guard(map)
print(guard.position)
