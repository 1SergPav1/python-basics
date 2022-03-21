# Задание № 1

with open('nginx_logs.txt', encoding='utf-8') as f:
    my_list = []
    [my_list.append((line.split()[0], line.split()[5][1:], line.split()[6])) for line in f]
    print(my_list[0:10])
    
