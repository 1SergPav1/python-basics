import re

my_email = '132@mail.ru'

REG = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

def email_parse(email):
    if REG.findall(email):
        tmp = (REG.findall(email))[0].split('@')
        print({'usergname': tmp[0], 'domain': tmp[1]})
    else:
        raise ValueError(f'wrong email {email}')

email_parse(my_email)
