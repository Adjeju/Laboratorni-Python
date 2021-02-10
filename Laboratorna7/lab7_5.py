import random

a = [list(map(float, input().split())) for i in range(8)]
c = []

for i in range(8):
    b = []
    for j in range(8):
        b.append(a[j][i])
    if b == a[i]:
        c.append(i)

print('k=',format(c))