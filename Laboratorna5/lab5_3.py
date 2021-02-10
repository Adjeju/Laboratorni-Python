import math

pi = math.pi
x = float(input('Введіть х від (-pi; pi): '))
while True:
    if -pi < x < pi:
        break
    else:
        x = float(input('Введіть х від (-pi; pi): '))
E = float(input('E= '))
i = 1
problem = 0
result = 0
while True:
    problem = (-1) ** (i - 1) * (math.sin(i * x)) / (i)
    result += problem
    if math.fabs(problem) < E:
        break
    i += 1

print('Значення суми - {0}'.format(result))
print("Кількість доданків - {0}".format(i))