class Geometric_Progression:
    def __init__(self, _first_elem = 0, _denominator = 0):
        self.first_elem = _first_elem
        self.denominator = _denominator

    def print_first_elem(self):
        self.first_elem = float(input('Enter first element: '))
        print('First element: {0}'.format(self.first_elem))

    def print_denominator(self):
        self.denominator = float(input('Enter denominator element: '))
        print('Denominator: {0}'.format(self.denominator))

    def get_n_element(self):
        n = int(input('Enter n for x(n) element: '))
        x_n = self.first_elem * self.denominator ** (n - 1)
        print('x({0}) = {1}'.format(n, x_n))
        return x_n

    def get_sum(self):
        n = int(input('Enter n for x(n) sum: '))
        s = (self.first_elem * (self.denominator ** n - 1)) / (self.denominator - 1)
        print('S({0}) = {1}'.format(n, s))

# geometric = Geometric_Progression()
# geometric.print_first_elem()
# geometric.print_denominator()
# x_n = geometric.get_n_element()
# sum = geometric.get_sum()

