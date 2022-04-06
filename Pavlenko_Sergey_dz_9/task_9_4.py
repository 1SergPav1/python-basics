# Задание 4

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Автомобиль поехал')

    def stop(self):
        print('Автомобиль остановился')

    def turn(self, direction):
        print(f'Автомобиль повернул {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed} км/ч')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость автомобиля {self.speed} км/ч \nПревышение скорости!')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость автомобиля {self.speed} км/ч \nПревышение скорости!')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


town_car = TownCar(65, 'grey', 'Ford Focus', False)
town_car.show_speed()
print(town_car.name)
print(town_car.color)

print('*' * 50)

work_car = WorkCar(45, 'yellow', 'JCB', False)
work_car.show_speed()
print(work_car.name)
print(work_car.color)

print('*' * 50)

sport_car = SportCar(150, 'Красная', 'Ferrari Enzo', False)
print(sport_car.name)
sport_car.show_speed()
