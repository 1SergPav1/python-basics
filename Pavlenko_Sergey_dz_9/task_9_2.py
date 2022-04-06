# Задание 2

class Road:
    def __init__(self, _weight, _length):
        self.weight = _weight
        self.length = _length

    def calc_mass_road(self):
        return f'{self.weight * self.length * 25 * 5} тонн'


a = Road(10, 20)

print(a.calc_mass_road())
