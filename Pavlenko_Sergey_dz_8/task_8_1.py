# Задание 1

import re

my_email = '132@mail.ru'

REG = re.compile(('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'))

def email_parse(email):
    try:
        tmp = (REG.findall(email))[0].split('@')
        print({tmp[0]: tmp[1]})
    except ValueError():
        print(f'wrong email {email}')

email_parse(my_email)
