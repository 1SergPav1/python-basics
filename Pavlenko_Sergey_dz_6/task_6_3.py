# Задание № 3

from itertools import zip_longest
my_dict = {}
my_list1 = []
my_list2 = []

with open('users.csv', encoding='utf-8') as f1:
    with open('hobbies.csv', encoding='utf-8') as f2:
        [my_list1.append(line.strip().replace(',', ' ')) for line in f1]
        [my_list2.append(line.strip()) for line in f2]

if len(my_list2) > len(my_list1):
    exit(1)
else:
    my_dict = dict(zip_longest(my_list1, my_list2))
    print(my_dict)

with open('result.csv', 'w', encoding='utf-8') as f3:
    f3.write(str(my_dict))
