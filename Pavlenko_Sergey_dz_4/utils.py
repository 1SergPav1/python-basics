import requests
import datetime


def currency_rates(val):
    val = val.upper()
    keys = []
    values = []

    # получим ответ от сервера и преобразуем в строку
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    # Из ответа сервера получим дату по индексу 3. Рзделим получившуюся строку по ".", преобразуем в тип int
    # и передадим аргументами в функцию для формирования объекта data
    date = content.split()[3].rstrip('"')[-10:]
    year, month, day = int(date.split('.')[2]), int(date.split('.')[1]), int(date.split('.')[0])
    date_obj = datetime.date(year, month, day)

    # проходим циклом по строке с ответом сервера и вытаскиваем из нее коды валют (ключи) и текущий курс (значения)
    # в соответствующие словари
    for i in content.split('/'):
        if i.startswith('NumCode'):
            keys.append(i[-4:-1])
        elif i.startswith('Name'):
            values.append(float(i.rstrip('<')[12:].replace(',', '.')))

    # соберем словарь код валюты : курс
    my_dict = dict(zip(keys, values))

    return print(my_dict.get(val), ',', date_obj)


if __name__ == '__main__':
    currency_rates('eur')
    currency_rates('USD')
