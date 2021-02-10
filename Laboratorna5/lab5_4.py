x0 = 0
x1 = 7
n = int(input('n= '))
for i in range(2, n+1):
    res = x1 * (1 + x0)
    x0, x1 = x1, res

print("x(n) = {0}".format(res))