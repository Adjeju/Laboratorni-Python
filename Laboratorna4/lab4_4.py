
x = float(input("Введіть х: "))
problem = 2 * x ** 2 - x - 3
def getResult(x):
    if problem == 0:
        y = 1
    elif problem > 0:
        y = 2
    elif problem < 0:
        y = 0
    return y

res = getResult(x)
print("Результат - {0}".format(res))