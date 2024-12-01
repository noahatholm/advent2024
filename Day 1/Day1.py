

def difference(num1,num2):
    return(abs(int(num1) - int(num2)))

def sim(num, array):
    return (int(num) * array.count(num))

def sum_array(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum

left = []
right = []
dif1 = []
dif2 = []

f = open("data.txt", "r")
for i in (f):
    split = i.split('   ')
    left.append(split[0])
    if split[1].endswith('\n'):
        split[1] = split[1][:-1]
    right.append(split[1])


left.sort()
right.sort()

for i in range(len(left)):
    dif1.append(difference(left[i],right[i]))

for i in range(len(left)):
    dif2.append(sim(left[i],right))

print(sum_array(dif1))

print(sum_array(dif2))


f.close()


