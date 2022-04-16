# Задание 3

import datetime
from functools import wraps

def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        with open('log.txt', 'a', encoding='utf-8') as file:
            for arg in args:
                log = f'{datetime.datetime.now()}: {func.__name__}({arg}: {type(arg)}) \n'
                file.write(log)

    return wrapper

@type_logger
def my_func(*args):
    s = sum(args)
    return s


my_func(4, 5)
