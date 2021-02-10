import random

n = int(input('n= '))
a = [[random.randint(1, 9) for j in range(n)] for i in range(n)]

for i in range(n):
    print(a[i])

print('-' * (n * 3))

for j in range(n):
    if j % 2 != 0:
        b = []
        for i in range(n):
            b.append(a[i][j])
        b = sorted(b, reverse= True)
        for i in range(n):
            a[i][j] = b[i]

for i in range(n):
    print(a[i])
