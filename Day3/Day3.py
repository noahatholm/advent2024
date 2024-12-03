import re

def readFile(filename):
    f = open(filename, "r")
    data = f.read()
    f.close()
    return data

def applyregex(data,pattern):
    match = re.findall(pattern, data)
    return match

def regexSplit(data,pattern):
    data = re.split(pattern,data)
    copy = []
    skip = False
    for i in range(len(data)):
        if skip == False:
            copy.append(data[i])
        skip = False
        
        if data[i] == "don't()":
            skip = True
    copy = ''.join(copy)
    return copy

def splitMul(data):
    sanitised =[]
    for i in range(len(data)):
        split = (data[i][4:-1]).split(',')
        sanitised.append(split)
    return sanitised

def mul(array):
    mul = 1
    for i in range(len(array)):
        mul = mul * int(array[i])
    return mul

def Sum(array):
    sum = 0
    for i in range(len(array)):
        sum += mul(array[i])
    return sum


def doNot(data):
    split = data.split("don't()")
    for i in range(len(split)):
        split = split[i].split("do()")
    return split

pattern1 = r"mul\(\d+,-?\d+\)"
pattern2 = r"(do\(\)|don't\(\))"

data = readFile("data.txt")

task2 = (regexSplit(data,pattern2))


task1 = applyregex(data,pattern1)
task2 = applyregex(task2,pattern1)



task1 = splitMul(task1)
task2 = splitMul(task2)
result1 = Sum(task1)
result2 = Sum(task2)

print(str(result1) + '\n' + str(result2))



