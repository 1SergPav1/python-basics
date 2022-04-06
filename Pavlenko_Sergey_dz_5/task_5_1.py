# Задание № 1

def odd_to_n(n):
    for num in range(1, n + 1, 2):
        yield num

odd_to = odd_to_n(15)

print(next(odd_to))
print(next(odd_to))
print(next(odd_to))
