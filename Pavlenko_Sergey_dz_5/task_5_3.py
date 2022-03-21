# Задание № 3

from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Евгений', 'Виктор'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
school = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses))

print(type(school))

print(next(school))
print(next(school))
print(next(school))
print(next(school))
print(next(school))
print(next(school))
print(next(school))
print(next(school))
print(next(school))
print(next(school))
