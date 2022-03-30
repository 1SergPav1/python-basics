# Задание 3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Worker name: {self.name} {self.surname}')

    def get_total_income(self):
        total_income = self._income["wage"] + self._income["bonus"]
        print(f'Total income: {total_income}')


driver = Position('Ivan', 'Romanov', 'driver', 15000, 10000)

driver.get_full_name()
driver.get_total_income()
