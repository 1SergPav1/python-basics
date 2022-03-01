# Задание № 3

def thesaurus(*args):
    names = []
    letters = []
    same_letter_names = []

    for arg in args:
        names.append(arg)  # заполним список для имен
        if arg[0] not in letters:
            letters.append(arg[0])  # заполним список для первых букв

    # создадим список со списками имен, начинающимися с одной буквы
    for letter in letters:
        same_letter_names.append(list(filter(lambda x: x.startswith(letter), names)))

    # соберем итоговый словарь - первая буква имени : имена начинающиеся с этой буквы
    result_dict = dict(zip(letters, same_letter_names))
    return result_dict


new_dict = thesaurus('Анна', 'Алексей', 'Александр', 'Петр', 'Василий', 'Владимир', 'Марина', 'Дима', 'Диана')
print(new_dict)
