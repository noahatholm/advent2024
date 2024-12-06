#dont have time to do task2 today friend is still visting 

def readFile(filename):
    with open(filename, "r") as f:
        data = f.read()
    data = data.split('\n') 
    data = [list(row) for row in data]
    return data

def findGuard(array):
    for y in range(len(array)):
        for x in range(len(array[y])):
            if array[y][x] == "^" or array[y][x] == ">" or array[y][x] == "V" or array[y][x] == "<":
                return [y,x,array[y][x]]
    return False

def checkBounds(array,x,y):
    if x < 0 or x > (len(array[0])-1):
        return True
    elif y < 0 or y > (len(array)-1):
        return True
    return False

def turnRight(facing):
    if facing == '^':
        return '>'
    elif facing == ">":
        return "V"
    elif facing == "V":
        return "<"
    elif facing == "<":
        return "^"
    else: facing = False
    return facing



def moveGuard(array,y,x,facing,directions):
    zx = x + directions[facing][1]
    zy = y + directions[facing][0]
    if checkBounds(array,zx,zy):
        return False
    if array[zy][zx] == "#":
        facing = turnRight(facing)
        zx = x + directions[facing][1]
        zy = y + directions[facing][0]
    array[zy][zx] = facing
    array[y][x] = "X"
    return array


def trackGuard(array,directions):
    while True:
        info = findGuard(array)
        copy = array
        array = moveGuard(array,info[0],info[1],info[2],directions)
        if array == False:
            return copy 

directions = {"^": [-1,0],">": [0,1],"V": [1,0],"<": [0,-1]}

data = readFile("data.txt")



data = trackGuard(data,directions)

count = 1
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "X":
            count += 1

print(count)