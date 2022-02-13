# Задание №2

cubes = []
num = 0

while num < 1000:
    if num % 2 != 0:
        cubes.append(num ** 3)
    num += 1
print(cubes)

# a

sum_numbers_cubes = []

for cube in cubes:
    sum_numbers = 0
    while cube > 0:
        sum_numbers += cube % 10
        cube //= 10
    if sum_numbers % 7 == 0:
        sum_numbers_cubes.append(sum_numbers)
print(sum_numbers_cubes)

# b

new_cubes = []
new_sum_numbers_cubes = []

for cube in cubes:
    cube += 17
    new_cubes.append(cube)
print('\n', new_cubes)

for cube in new_cubes:
    sum_numbers = 0
    while cube > 0:
        sum_numbers += cube % 10
        cube //= 10
    if sum_numbers % 7 == 0:
        new_sum_numbers_cubes.append(sum_numbers)
print(new_sum_numbers_cubes)

# c

sum_numbers_cubes = []

for cube in cubes:
    cube += 17
    sum_numbers = 0
    while cube > 0:
        sum_numbers += cube % 10
        cube //= 10
    if sum_numbers % 7 == 0:
        sum_numbers_cubes.append(sum_numbers)
print('\n', sum_numbers_cubes)
