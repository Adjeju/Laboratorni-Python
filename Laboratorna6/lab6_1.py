n = int(input('n= '))
a = [float(input('a[{0}]='.format(i))) for i in range(n)]
el_count = 0

for i in range(len(a) - 2):
    if a[i+1] - a[i] == a[i+2] - a[i+1]:
        el_count += 1

print('Кількість пар з трьох елементів, які слідують підряд і утворюють арифметичну прогресію: {0}'.format(el_count))
