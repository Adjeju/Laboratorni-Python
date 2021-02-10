a = float(input("a= "))
b = float(input("b= "))
c = float(input("c= "))

def getMin(x, y):
    if x>y:
        min = y
    else:
        min = x
    return min

res = getMin(a, b) + (getMin(b, c))**2
print('Result - {0}'.format(res))