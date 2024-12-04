def readFile(filename):
    f = open(filename, "r")
    data = f.read()
    data = data.split('\n')
    f.close()
    return data


def search(x,y,dx,dy,word,array):
    if array[y][x] != word[0]:
        return False
    else:
        zx = x + dx
        zy = y + dy
        for i in range(1,len(word)):

            if (zx < 0 or zy < 0 or zx >= len(array[y]) or zy >= len(array)):
                return False
            else:
                if(array[zy][zx] != word[i]):
                    return False
            zx = zx + dx
            zy = zy + dy
        return True



def initsearch(word,array,directions):
    count = 0
    for y in range(len(array)):
        for x in range(len(array[y])):
            for dx, dy in directions:
                if search(x,y,dx,dy,word,array):
                    count += 1
    return count
                


def masSearch(mas,array):
    count = 0
    for y in range(1,len(array)-1):
        for x in range(1, len(array)-1):
            if array[y][x] == mas[1]:
                if checkX(array,mas[0],mas[2],x,y):
                    count += 1
    return count


def checkX(array,M,S,x,y):
    pattern = (array[y-1][x-1], array[y][x], array[y+1][x+1], array[y+1][x-1], array[y-1][x+1])
    if pattern in [
        ('M', 'A', 'S', 'M', 'S'), ('S', 'A', 'M', 'M', 'S'), ('M', 'A', 'S', 'S', 'M'), ('S', 'A', 'M', 'S', 'M'),]:
        return True
    return False



word = 'XMAS'
mas = 'MAS'
filename = 'data.txt'
directions = [(0, 1), (0, -1),(1, 0),(-1, 0),(1, 1),(-1, -1),(1, -1), (-1, 1)]



data = readFile('data.txt')

print(initsearch(word,data,directions))
print(masSearch(mas,data))

