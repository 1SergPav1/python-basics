# Задание №1

duration = int(input('Введите длительность временного промежутка в секундах: '))
minute = duration // 60
hours = duration // 3600
days = duration // 86400
if duration < 60:
    seconds = duration
    print(seconds, 'сек')
elif 60 <= duration < 3600:
    seconds = duration % 60
    print(minute, 'мин', seconds, 'сек')
elif 3600 <= duration < 86400:
    seconds = duration % 60
    minute = minute % 60
    print(hours, 'час', minute, 'мин', seconds, 'сек')
else:
    seconds = duration % 60
    minute = minute % 60
    hours = duration % 86400 // 3600
    print(days, 'дн', hours, 'час', minute, 'мин', seconds, 'сек')
