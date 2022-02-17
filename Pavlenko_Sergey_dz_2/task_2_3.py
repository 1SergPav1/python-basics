# Задание № 3

old_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+05', 'градусов']
word = ''
number = ''
index = -1

for i in old_list:
    index += 1
    if i.isdigit() == True:
        old_list[index] = f'"{int(i):02d}"'
    elif i.isalnum() == False:
        for j in i:
            if j.isdigit() == False:
                word += j
            else:
                number += j
        old_list[index] = f'"{word}{int(number):02d}"'

my_str =' '.join(old_list)
print(my_str)
