n = int(input('n= '))
a = [-4, 3]
new = []
s = 0
def getInterval():
    b = int(input('b= '))
    c = int(input('c= '))
    return b, c

b, c = getInterval()

for i in range(2, n+1):
    res = a[i-1]**2 + 2 * a[i-2] - i
    a.append(res)

for el in a:
    if b < el <= c:
        s += el
        new.append(el)

avarage = s / len(new)
print('Середнє значення: {0}'.format(avarage))