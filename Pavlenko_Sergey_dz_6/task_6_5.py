# Задание № 5

import sys
from itertools import zip_longest

names = []
surnames = []
patronymics = []
full_name = []
hobbies = []
result_dict = {}

users_file, hobbies_file, result_file = sys.argv[1:]

with open(users_file, encoding='utf-8') as f1:
    with open(hobbies_file, encoding='utf-8') as f2:
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

with open(result_file, 'w', encoding='utf-8') as f:
    f.write(str(result_dict))
