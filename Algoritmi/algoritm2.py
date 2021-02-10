import random
import math

n = int(input('n = '))
a = [[random.randint(1, 9) for j in range(n)] for i in range(n)]
b = []

for i in range(len(a)):
    print(a[i])

for i in range(math.ceil(n/2)):
    b.extend(a[i][0 : i + 1])
    b.extend(a[n - i - 1][0 : i + 1])

b[-math.ceil(n/2) : ] = []

print('Сума: {0}'.format(sum(b)))
print('Максимальний елемент: {0}'.format(max(b)))