# Задание 5

class Stationery:
    def __init__(self, tittle):
        self.tittle = tittle

    def draw(self):
        print('Запуск отрисовки.')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки. Карандаш рисует.')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки. Ручка рисует.')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки. Маркер рисует.')


pen = Pen('ручка')
pen.draw()

pencil = Pencil('карандаш')
pencil.draw()

handle = Handle('маркер')
handle.draw()
