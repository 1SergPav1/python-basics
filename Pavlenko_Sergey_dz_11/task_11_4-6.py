# Задание 4-6

class Stock:  # класс склад
    def __init__(self):
        self.my_storage_dict = {}

    def __str__(self):
        return f'{self.my_storage_dict}'

    def add_to_storage(self, equipment):  # метод для добавления оргтехники на склад
        if equipment.type_name not in self.my_storage_dict.keys():
            self.my_storage_dict[equipment.type_name] = {equipment.model_name: equipment.amount}
        else:
            if equipment.model_name in self.my_storage_dict[equipment.type_name].keys():
                self.my_storage_dict.get(equipment.type_name)[equipment.model_name] += equipment.amount
        self.my_storage_dict[equipment.type_name].setdefault(equipment.model_name, equipment.amount)
        return self.my_storage_dict

    def take_from_storage(self, equipment):  # метод для передачи оргтехники со склада на сторону
        if equipment.type_name not in self.my_storage_dict.keys():
            print('Такой позиции нет на складе1')
        elif equipment.model_name not in self.my_storage_dict[equipment.type_name].keys():
            print('Такой позиции нет на складе2')
        else:
            self.my_storage_dict.get(equipment.type_name)[equipment.model_name] -= equipment.amount
        return self.my_storage_dict


class OfficeEquipment:
    def __init__(self, type_name, model_name, amount):
        self.type_name = type_name  # тип оргтехники (принтер, сканер, ксерокс)
        self.model_name = model_name  # модель конкретной единицы оргтехники
        try:
            self.amount = amount  # кол-во единиц данной модели оргтехники
            if type(self.amount) != int:
                raise TypeError
        except TypeError:
            print('Последний аргумент (число единиц техники) должен быть целым числом')

    def __str__(self):
        return f'Наименование - {self.type_name}\nМодель - {self.model_name}\nКоличество - {self.amount} штук'


class Printer(OfficeEquipment):
    def __init__(self, model_name, amount):
        self.model_name = model_name
        try:
            self.amount = amount
            if type(self.amount) != int:
                raise TypeError
        except TypeError:
            print('Последний аргумент (число единиц техники) должен быть целым числом')
        self.type_name = 'Printer'


class Scanner(OfficeEquipment):
    def __init__(self, model_name, amount):
        self.model_name = model_name
        try:
            self.amount = amount
            if type(self.amount) != int:
                raise TypeError
        except TypeError:
            print('Последний аргумент (число единиц техники) должен быть целым числом')
        self.type_name = 'Scanner'


class Copier(OfficeEquipment):
    def __init__(self, model_name, amount):
        self.model_name = model_name
        try:
            self.amount = amount
            if type(self.amount) != int:
                raise TypeError
        except TypeError:
            print('Последний аргумент (число единиц техники) должен быть целым числом')
        self.type_name = 'Copier'


hp_lj = Printer('HP LJ 1100', 10)
print(hp_lj)
hp_lj_1 = Printer('HP LJ 2100', 20)
hp_lj_2 = Printer('HP LJ 1100', 40)
hp_lj_3 = Printer('HP LJ 2100', 50)

my_stock = Stock()
my_stock.add_to_storage(hp_lj)
my_stock.add_to_storage(hp_lj_1)
my_stock.add_to_storage(hp_lj_2)
my_stock.add_to_storage(hp_lj_3)

epson = Scanner('Epson 80W', 5)
my_stock.add_to_storage(epson)

xerox = Copier('Xerox WorkCentre', 7)
my_stock.add_to_storage(xerox)

print(my_stock)

kodac = Printer('kodac', 'gyu') # второй аргумент (кол-во единиц техники) вместо int - str

print(my_stock.take_from_storage(hp_lj_1))
