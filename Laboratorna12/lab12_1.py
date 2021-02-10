class Ttime:
    def __init__(self, hours = 13, minutes = 0):
        self.hours = hours
        self.minutes = minutes

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value):
        if 0 <= value < 24:
            self.__hours = value
        else:
            raise Exception('Error')

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, value):
        if 0 <= value < 60:
            self.__minutes = value
        else:
            raise Exception('Error')

    def get_and_print(self):
        self.hours = int(input('Hours = '))
        self.minutes = int(input('Minutes = '))
        print('{0}:{1}'.format(self.hours, self.minutes))

    def add_hours(self):
        hours = int(input('Hours to add = '))
        minutes = int(input('Minutes to add = '))
        self.hours += hours
        self.minutes += minutes
        if 0 > self.hours > 24 and 0 > self.minutes > 60:
            print('Error')
        else:
            print('{0}:{1}'.format(self.hours, self.minutes))


time = Ttime()
time.get_and_print()
time.add_hours()