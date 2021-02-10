n = int(input('n = '))
res = 0
a1 = 1

for i in range(2, n + 1):
    if i % 2 != 0:
        res -= i
    else:
        res += i

res += a1
print(res)