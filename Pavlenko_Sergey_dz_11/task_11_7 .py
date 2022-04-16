# Задание 7

class Compl:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im > 0:
            return f'{self.re}+{self.im}i'
        else:
            return f'{self.re}{self.im}i'

    def __add__(self, other):
        return Compl(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return Compl((self.re * other.re - self.im * other.im), (self.re * other.im + self.im * other.re))


a = Compl(4, -9)
print(a)

b = Compl(2, 7)
print(b)

c = a + b
print(c)

d = a * b
print(d)
