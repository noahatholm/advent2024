left = []
right = []
dif = []

def difference(num1,num2):
    return(abs(int(num1) - int(num2)))

def sum_array(array):
    sum = 0
    for i in range(len(dif)):
        sum += dif[i]
    return sum

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
    dif.append(difference(left[i],right[i]))


print(sum_array(dif))


f.close()