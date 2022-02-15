# Задание №2

cubes = []
num = 0

while num < 1000:
    if num % 2 != 0:
        cubes.append(num ** 3)
    num += 1
print(cubes)

# a

new_cubes = []
sum_cubes = 0

for cube in cubes:
    sum_numbers = 0
    temp_cube = cube
    while temp_cube > 0:
        sum_numbers += temp_cube % 10
        temp_cube //= 10
    if sum_numbers % 7 == 0:
        new_cubes.append(cube)
print('\n', new_cubes)

for cube in new_cubes:
    sum_cubes += cube
print('а) Сумма кубов из списка, сумма цифр которых делится нацело на 7 =', sum_cubes)

# b

temp_cubes = []
new_cubes = []
sum_cubes = 0

for cube in cubes:
    temp_cube = cube + 17
    temp_cubes.append(temp_cube)

for cube in temp_cubes:
    sum_numbers = 0
    temp_cube = cube
    while temp_cube > 0:
        sum_numbers += temp_cube % 10
        temp_cube //= 10
    if sum_numbers % 7 == 0:
        new_cubes.append(cube)
print('\n', new_cubes)

for cube in new_cubes:
    sum_cubes += cube
print('b) Сумма кубов из списка, сумма цифр которых делится нацело на 7 =', sum_cubes)

# c

new_cubes = []
sum_cubes = 0

for cube in cubes:
    sum_numbers = 0
    temp_cube = cube + 17
    while temp_cube > 0:
        sum_numbers += temp_cube % 10
        temp_cube //= 10
    if sum_numbers % 7 == 0:
        new_cubes.append(cube + 17)
print('\n', new_cubes)

for cube in new_cubes:
    sum_cubes += cube
print('c) Сумма кубов из списка, сумма цифр которых делится нацело на 7 =', sum_cubes)

