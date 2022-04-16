# Задание 4

import os

file_sizes = []
dict_sizes = {}
temp = []

for r, d, f in os.walk('./'):
    for file in f:
        file_sizes.append(os.stat(os.path.join(r, file)).st_size) # добавляем в список значения размеров всех файлов

max_size = max(file_sizes) # получаем значение самого большого файла
i = 1

for j in range(len(str(max_size))): # получим старший разряд значения размера самого большого файла, пройдем по разрядам в цикле
    # и для каждого разряда создадим ключ в словаре
    i *= 10
    dict_sizes[i] = 0

for file in file_sizes:
    dict_sizes[10 ** len(str(file))] += 1 # проходим циклом по списку с значениями размеров файлов, опеределяем старший
    # разряд значения и увеличиваем на единицу значение соответсвующего разрядности ключа

print(dict_sizes)
