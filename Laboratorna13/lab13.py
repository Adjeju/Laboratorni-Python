import math
class TCircle:
    def __init__(self, r = 1):
        self.r = r

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, value):
        if value <= 0:
            raise Exception('Error')
        else:
            self.__r = value

    def get_and_print(self):
        self.r = float(input('r = '))
        print('Radius: {0}'.format(self.r))

    def get_s_circle(self):
        s_circle = 3.14 * (self.r ** 2)
        print('Quare: {0}'.format(s_circle))
        return s_circle

    def get_len_circle(self):
        len_circle = 2 * 3.14 * self.r
        print('Length: {0}'.format(len_circle))

    def __lt__(self, other):
        return self.r < other.r

    def __add__(self, other):
        return (other + self.r)

    def __sub__(self, other):
        return (self.r - other)

    def __mul__(self, other):
        return (other * self.r)

class TCylinder(TCircle):
    def __init__(self, r = 1, h = 1):
        super().__init__(r)
        self.h = h

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, value):
        if value <= 0:
            raise Exception('Error')
        else:
            self.__h = value

    def get_and_print(self):
        self.r = float(input('r = '))
        self.h = float(input('h = '))
        print('Radius: {0}, height: {1}'.format(self.r, self.h))

    def get_v_cilinder(self):
        v_cylinder = super().get_s_circle() ** 2 * 3.14 * self.h
        print('v Cylinder: {}'.format(v_cylinder))

circle1 = TCircle()
circle1.get_and_print()
circle2 = TCircle()
circle2.get_and_print()
if circle1 > circle2:
    print("Circle1 > Circle2")
else:
    print("Circle1 < Circle2")
cylinder = TCylinder()
cylinder.get_and_print()
cylinder.get_v_cilinder()
