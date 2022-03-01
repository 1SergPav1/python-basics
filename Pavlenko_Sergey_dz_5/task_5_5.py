# Задание № 5

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_src = []
[new_src.append(i) for i in src if i not in new_src]

print(new_src)
