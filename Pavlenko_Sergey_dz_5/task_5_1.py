# Задание № 1

def odd_to_n():
    for num in range(1, 15 + 1, 2):
        yield num

odd_to = odd_to_n()

print(next(odd_to))
print(next(odd_to))
print(next(odd_to))
