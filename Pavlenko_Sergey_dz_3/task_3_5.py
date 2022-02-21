# Задание № 5

from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n=1, r=1):
    """
        Возвращает n шуток, сформированных их трех случайных слов,
        взятых из трех списков (по одному из каждого).

            Параметры:
                    n (int): количество шуток
                    r (int): разрешить (1) или запретить (0) повторы слов в шутках

            Возвращаемое значение:
                    joke_list (list): список содержащий n шуток
    """

    joke_list = []

    if r == 1:
        for i in range(n):
            joke = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
            joke_list.append(joke)
        print(joke_list)

    if r == 0:
        for i in range(n):
            word_1, word_2, word_3 = choice(nouns), choice(adverbs), choice(adjectives)
            nouns.remove(word_1)
            adverbs.remove(word_2)
            adjectives.remove(word_3)
            joke = f'{word_1} {word_2} {word_3}'

            joke_list.append(joke)
        print(joke_list)


get_jokes(4, 0)

