# Задание № 2

old_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
word = ''
number = ''

for i in old_list:
    if i.isdigit() == True:
        i = f'"{int(i):02d}"'
        new_list.append(i)
    elif i.isalnum() == False:
        for j in i:
            if j.isdigit() == False:
                word += j
            else:
                number += j
        i = f'"{word}{int(number):02d}"'
        new_list.append(i)
    else:
        new_list.append(i)

my_str =' '.join(new_list)
print(my_str)
