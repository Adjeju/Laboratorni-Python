import datetime

class RAM:
    def __init__(self, _date, _manufacturer = 'no name', _storage = 1, _price = 0):
        self.manufacturer = _manufacturer
        self.date = _date
        self.storage = _storage
        self.price = _price

    def get_value(self):
        gb_storage = self.storage / 1024
        kb_storage = 1024 * self.storage
        bb_storage = self.storage / (1024 * 1024 * 8)
        print(gb_storage)
        print(kb_storage)
        print(bb_storage)

    def get_converte(self):
        type_of = input('type = ')
        value = int(input("value = "))
        if type_of.lower() == 'gb':
            mb_value = value / 1024
            if self.storage > mb_value or self.storage == mb_value:
                print('Information will fit')
            else:
                print("Information won't fit")
        elif type_of.lower() == 'kb':
            mb_value = 1024 * self.storage
            if self.storage > mb_value or self.storage == mb_value:
                print('Information will fit')
            else:
                print("Information won't fit")
        elif type_of.lower() == 'bb':
            mb_value = self.storage / (1024 * 1024 * 8)
            if self.storage > mb_value or self.storage == mb_value:
                print('Information will fit')
            else:
                print("Information won't fit")
        else:
            print('Error')

    def ram_age(self):
        now = datetime.date.today()
        delta = now - self.date
        return delta

# ram = RAM(datetime.date(2000, 1, 17))
# ram.get_value()
# ram.get_converte()
# delta = ram.ram_age()
# print('Delta of time: {0}'.format(delta))
