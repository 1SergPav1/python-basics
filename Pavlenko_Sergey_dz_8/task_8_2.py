# Задание 2

import re

REG = re.compile(r'((?:[0-9]{,3}[\.]){3}[0-9]{,3}) - - ' # ip
                 r'(.[0-9]{,2}[\/][A-Za-z]{3}[\/][0-9]{4}:(?:[0-9]{2}:){2}[0-9]{2} \+[0-9]{4}]) .' # date
                 r'([A-Z]{3}) ' # type
                 r'([\/A-Za-z]+_\d) .+ ' # resource
                 r'([0-9]{3} ' # response code
                 r'[0-9]{,4}) ') # response_size

with open('nginx_logs.txt') as file:
    with open('result.txt', 'w', encoding='utf-8') as f:
        for line in file:
            raw = REG.findall(line)
            f.write(str(raw) + '\n')
