import random

n = int(input('n= '))
a = [random.randint(0,100) for i in range(n)]
b = []

for i in range(len(a)):
    if i % 2 != 0:
        b.append(a[i])

for i in range(len(a)):
    if i % 2 == 0:
        b.append(a[i])
print(a)
print(b)