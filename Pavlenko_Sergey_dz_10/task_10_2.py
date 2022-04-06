# Задание 2

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def calculation(self):
        pass


class Coat(Clothes):
    @property
    def calculation(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    @property
    def calculation(self):
        return 2 * self.size + 0.3


a = Coat(15)
print(a.calculation)

b = Suit(25)
print(b.calculation)
