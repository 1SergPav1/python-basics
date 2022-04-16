# Задание 2

class MyDivivsion:
    def __init__(self, num_1, num_2):
        self.num1 = num_1
        self.num2 = num_2

    def div(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            print('Делить на ноль нельзя!')


a = MyDivivsion(1, 2)
b = MyDivivsion(1, 0)
print(a.div())
print(b.div())

