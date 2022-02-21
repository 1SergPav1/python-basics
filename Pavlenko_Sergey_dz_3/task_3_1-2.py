# Задание № 1 - 2

def num_translate(num):
    nums = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    print(f'{nums.get(num.lower(), "Перевод невозможен")}'.capitalize()) if num[0].istitle() == True else print(
        nums.get(num, "Перевод невозможен"))


user_num = input('Введите числительное от 1 до 10 на английском: ')
num_translate(user_num)
