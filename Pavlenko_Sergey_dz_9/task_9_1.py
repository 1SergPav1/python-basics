# Задание 1

import time


class Traffic:
    __color = ['red', 'yellow', 'green']

    def runnig(self, color):
        while True:
            print(color[0])
            time.sleep(7)
            print(color[1])
            time.sleep(2)
            print(color[2])
            time.sleep(5)


a = Traffic()
a.runnig(a._Traffic__color)
