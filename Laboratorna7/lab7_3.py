import random

row = int(input('row= '))
cols = int(input('cols= '))
num = int(input('number= '))
a = []

for i in range(row):
    row = []
    for j in range(cols):
        elem = random.randint(1,9)
        row.append(elem * num)
    a.append(row)

for i in range(len(a)):
    print(a[i])