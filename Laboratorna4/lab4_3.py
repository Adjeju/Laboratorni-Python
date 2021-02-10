x1 = float(input('x1= '))
y1 = float(input('y1= '))
x2 = float(input('x2= '))
y2 = float(input('y2= '))
x3 = float(input('x3= '))
y3 = float(input('y3= '))

def getResult(x1, y1, x2, y2):
    lenght = ((x2 - x1) **2 + (y2-y1)**2)**(1/2)
    return lenght

AB = getResult(x1, y1, x2, y2)
BC = getResult(x2, y2, x3, y3)
AC = getResult(x3, y3, x1, y1)

P = round(AB + BC + AC, 2)

print("Периметр - {}".format(P))