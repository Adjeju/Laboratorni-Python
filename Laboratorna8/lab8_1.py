def getMax(x,y):
    '''
    Func for getting max of 2 arguments
    :param x: first argument
    :param y: second argument
    :return: max of 2 arguments
    '''
    if x > y:
        max = x
    else:
        max = y

x = int(input('x= '))
y = int(input('y= '))
z = int(input('z= '))

res = (getMax(x, z) + getMax(x + y, x * y)) / getMax(x + y, x * y) ** 2

print('Результат: {0}'.format(res))