class Poligon:
    def __init__(self, *args):
        self.len_sides = len(args)
        if self.len_sides == 0 or self.len_sides == 1 or self.len_sides == 2:
            raise Exception('Error')
        elif self.len_sides == 3:
            self.a = args[0]
            self.b = args[1]
            self.c = args[2]
        elif self.len_sides == 4:
            self.a = args[0]
            self.b = args[1]
            self.a = args[2]
            self.d = args[3]

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if value <= 0:
            raise Exception("Error")
        else:
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if value <= 0:
            raise Exception("Error")
        else:
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if value <= 0:
            raise Exception("Error")
        else:
            self.__c = value

    @property
    def d(self):
        return self.__d

    @d.setter
    def d(self, value):
        if value <= 0:
            raise Exception("Error")
        else:
            self.__d = value

    def __getitem__(self, item):
        if item == 1:
            return self.a
        elif item == 2:
            return self.b
        elif item == 3:
            return self.c
        elif item == 4:
            return self.d

    def get_and_print(self):
        if self.len_sides <= 2:
            raise Exception('Eeoeoeoeoe')
        elif self.len_sides == 3:
            self.a = int(input('a = '))
            self.b = int(input('b = '))
            self.c = int(input('c = '))
            print('Triangle ({0},{1},{2})'.format(self.a, self.b, self.c))
            P = self.a + self.b + self.c
            p = (self.a + self.b + self.c) / 2
            s = (p * (p - self.a) * (p - self.a) * (p - self.a)) ** 0.5
            print("P of triangle: {0}, S of triangle: {1}".format(P,s))
        elif self.len_sides == 4:
            self.a = int(input('a = '))
            self.b = int(input('b = '))
            self.c = int(input('c = '))
            self.d = int(input('d = '))
            if self.a == self.b == self.c == self.d:
                p = 4 * self.a
                s = self.a ** 2
                print('S and P of Squere: {0} & {1}'.format(p,s))
            elif self.a == self.c and self.b == self.d:
                p = 2 * (self.a + self.b)
                s = self.a * self.b
                print('S and P of Rectangle: {0} & {1}'.format(p, s))
            else:
                raise Exception("Error")

fig = Poligon(1, 2, 3, 4)
fig.get_and_print()