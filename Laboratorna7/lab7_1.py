row = int(input('row= '))
cols = int(input('cols= '))
a = [[int(input('a[{0}][{1}]= '.format(i, j))) for j in range(cols)] for i in range(row)]
res = 1

for i in range(len(a)):
    for j in range(cols):
        if a[i][j] > 0 and a[i][j] % 2 == 0:
            res *= a[i][j]

print('Добуток додатних парних елементів матриці - {0}'.format(res))