# Задание 1

class Date:
    def __init__(self, date):
        self.date = date
        if not type(self.date) == str:
            raise TypeError('Укажите дату в виде строки формата «день-месяц-год»')

    @classmethod
    def transfer(cls, date):
        return list(map(int, date.split('-')))

    @staticmethod
    def valid(date):
        tmp_lst = Date.transfer(date)
        return True if tmp_lst[0] in range(1, 31) and tmp_lst[1] in range(1, 12) and tmp_lst[2] > 0 else False


my_date = '01-10-2022'
print(Date.transfer(my_date))
print(Date.valid(my_date))
