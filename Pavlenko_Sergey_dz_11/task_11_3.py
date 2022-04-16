# Задание 3

class NumList(Exception):

    @staticmethod
    def add_data_in_list():
        num_list = []
        while True:
            try:
                num = input('Введите число (или stop для выхода): ')
                if num == 'stop':
                    break
                num_list.append(int(num))
            except ValueError:
                print('Вы ввели не число!')
        return num_list


print(NumList.add_data_in_list())
