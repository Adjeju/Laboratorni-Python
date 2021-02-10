import math
class TCircle:
    def __init__(self, r, *args):
        self.r = r
        len_args = len(args)
        if len_args == 2:
            self.x = args[0]
            self.y = args[1]
        else:
            raise Exception('Error')

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, value):
        if value < 0 or value == 0:
            raise Exception('Error')
        else:
            self.__r = value

    def get_and_print(self):
        self.r = float(input('r = '))
        self.x = float(input('x = '))
        self.y = float(input('y = '))
        print('Radius: {0}, coordinates ({1}, {2})'.format(self.r, self.x, self.y))

    def get_s_circle(self):
        s_circle = 3.14 * (self.r ** 2)
        print('Quare: {0}'.format(s_circle))

    def get_nalezhnist(self, x, y):
        x = float(input("x = "))
        y = float(input("y = "))
        h = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
        print("Відстань від точки: {0}".format(h))
        if self.r > h:
            print("Точка ({0},{1}) належить кругу".format(x,y))
        else:
            print("Точка ({0},{1}) не належить кругу".format(x,y))

    def __add__(self, other):
        return (other + self.r)

    def __sub__(self, other):
        return (self.r - other)

    def __mul__(self, other):
        return (other * self.r)

circle = TCircle(1,0,0)
circle.get_and_print()
circle.get_s_circle()
circle.get_nalezhnist(3, 4)
print(circle + 5)
print(circle - 5)
print(circle * 5)