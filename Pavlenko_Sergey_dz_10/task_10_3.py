# Задание 3

class Cell:
    def __init__(self, nucleus):
        self.nucleus = nucleus
        if not type(self.nucleus) == int:
            raise TypeError('Кол-во ячеек в клетке должно быть целым числом')

    def __add__(self, other):
        return Cell(self.nucleus + other.nucleus)

    def __sub__(self, other):
        if not self.nucleus - other.nucleus > 0:
            print('Число ячеек в клетке не может быть меньше 0')
        return Cell(self.nucleus - other.nucleus)

    def __mul__(self, other):
        return Cell(self.nucleus * other.nucleus)

    def __floordiv__(self, other):
        return Cell(self.nucleus // other.nucleus)

    def __truediv__(self, other):  # метод __truediv__ повторяет __floordiv__ поскольку кол-во ячеек после деления
        # должно оставаться целым числом
        return Cell(self.nucleus // other.nucleus)

    def make_order(self):
        lines = self.nucleus // 5
        remainder = self.nucleus % 5
        for _ in range(lines):
            print(f'{5 * "*"}')
        if remainder != 0:
            print(f'{remainder * "*"}')


a = Cell(3)
b = Cell(3)
c = a + b
c.make_order()
print('-' * 10)
d = a * b
d.make_order()
print('-' * 10)
e = a // b
e.make_order()
print('-' * 10)
f = a - b
f.make_order()
