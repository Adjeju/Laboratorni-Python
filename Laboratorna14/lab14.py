import random
import numpy as np

class TMatrix:
    def __init__(self, num = 3):
        self.num = num

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, value):
        if value > 0:
            self.__num = value
        else:
            raise Exception('Error')

    def set_matrix(self):
        self.matrix = np.array([[random.randint(-10, 10) for i in range(self.num)] for i in range(self.num)])

    def get_sum_of_matrix(self):
        sum = np.sum(self.matrix)
        return sum

    def get_deter(self):
        deter = np.linalg.det(self.matrix)
        return deter

class TMatrix2(TMatrix):
    def __init__(self, num):
        super().__init__(num)

class TMatrix3(TMatrix):
    def __init__(self, num):
        super().__init__(num)

matrix2 = TMatrix2(2)
matrix2.set_matrix()
matrix3 = TMatrix3(3)
matrix3.set_matrix()

result = matrix3.get_sum_of_matrix() + matrix2.get_deter() + matrix3.get_deter()
print("Result: {0}".format(round(result, 2)))