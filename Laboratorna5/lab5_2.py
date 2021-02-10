x = int(input('x= '))
y = int(input('y= '))
countX_0 = 0
countY_0 = 0

while x > 0:
    c = x % 10
    if c == 0:
        countX_0 += 1
    x = x // 10

while y > 0:
    b = y % 10
    if b == 0:
        countY_0 += 1
    y = y // 10

if countX_0 > countY_0:
    print('X містить більшу кількість 0 ніж У')
elif countY_0 > countX_0:
    print('Y містить більшу кількість 0 ніж X')
elif countY_0 == countX_0:
    print('Х та У містить однакову кількість 0')