import math

row = int(input('row= '))
cols = int(input('cols= '))
n = int(input('n= '))
a = []
b = []
for i in range(1, row + 1):
    row = []
    for j in range(1, cols + 1):
        elem = round(j * math.cos(i ** 2 + n), 3)
        row.append(elem)
    a.append(row)

for i in range(len(a)):
    for j in range(cols):
        if (i + j) % 2 != 0:
            b.append(a[i][j])

for i in range(len(a)):
    print(a[i])

print('Сума елементів матриці А, сума індексів яких непарна: {0}'.format(sum(b)))