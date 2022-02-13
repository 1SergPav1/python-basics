Задание 3

for num in range(1, 101):
    if num % 10 == 1 and num not in range(11, 21):
        print(num, 'процент')
    elif num % 10 in range(2, 5) and num not in range(11, 21):
        print(num, 'процента')
    else:
        print(num, 'процентов')
        
