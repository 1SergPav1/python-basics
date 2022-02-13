# Задание №1

duration = int(input('Введите длительность временного промежутка в секундах: '))
if duration < 60:
    print('duration = {} сек'.format(duration))
elif 60 <= duration < 3600:
    print('duration = {} мин {} сек'.format(duration // 60, duration % 60))
elif 3600 <= duration < 86400:
    print('duration = {} час {} мин {} сек'.format(duration // 3600, duration % 3600 // 60, duration % 60))
else:
    print('duration = {} дн {} час {} мин {} сек'.format(duration // 86400, duration % 86400 // 3600,
                                                         duration % 3600 // 60, duration % 60))
