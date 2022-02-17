# Задание № 5

prices = [57.8, 46.51, 97, 150.73, 142.36, 779.91, 20.12, 947.40, 193.48, 25]
descending_prices = []
new_prices_str_list = []
index = -1

# преобразуем числа из списка в строки и создадим новый список со строками в нужном нам формате
for i in prices:
    i = str(i)
    index += 1
    i = f' {int(prices[index])} руб {int((prices[index] - int(prices[index])) * 100):02d} коп'
    new_prices_str_list.append(i)

# преобразуем полученный список в строку и выведем ее на экран
ascending_prices_str = ', '.join(new_prices_str_list)
print('\n', ascending_prices_str)

# отсортируем исходный список по возрастанию цены
prices.sort()

# перезапишем список со строками (чтобы не создавать новый список) и выведем строку с ценами по возрастанию
index = -1
for i in prices:
    i = str(i)
    index += 1
    new_prices_str_list[index] = f' {int(prices[index])} руб {int((prices[index] - int(prices[index])) * 100):02d} коп'

ascending_prices_str = ', '.join(new_prices_str_list)
print('\n', ascending_prices_str)

# cоздадим новый список, содержащий те же цены, но отсортированные по убыванию из полученной строки
descending_price_list = ascending_prices_str.split(', ')
descending_price_list.reverse()

# и выведем в виде строки
descending_prices_str = ', '.join(descending_price_list)
print('\n', descending_prices_str)

# выведем цены пяти самых дорогих товаров
dearest_prices_list = descending_price_list[:5]
dearest_prices_str = ', '.join(dearest_prices_list)
print('\n', dearest_prices_str)
