import random

a = []

for i in range(8):
    row = []
    for j in range(8):
        elem = random.randint(-1, 10)
        row.append(elem)
    a.append(row)

for i in range(len(a)):
    print(a[i])

for i in range(8):
    for j in range(8):
        if a[i][j] < 0:
            print('сума a[{0}] рядку: {1}'.format(i, sum(a[i])))
            break