# Задание № 4

from itertools import zip_longest

names = []
surnames = []
patronymics = []
full_name = []
hobbies = []
result_dict = {}

with open('users.csv', encoding='utf-8') as f1:
    with open('hobbies.csv', encoding='utf-8') as f2:
        [[names.append(line.strip().split(',')[0]),
          surnames.append(line.strip().split(',')[1]),
          patronymics.append(line.strip().split(',')[2])] for line in f1]
        [hobbies.append(line.strip()) for line in f2]

if len(names) < len(hobbies):
    exit(1)
else:
    [full_name.append(f'{names[i]} {surnames[i]} {patronymics[i]}') for i in range(len(names))]
    result_dict = dict(zip_longest(full_name, hobbies))

print(result_dict)
