# Задание 1
def num_translate(number):
    interpreter = {
        'one':'Один',
        'two':'Два',
        'three':'Три',
        'four':'Четыре',
        'five':'Пять',
        'six':'Шесть',
        'seven':'Семь',
        'eight':'Восемь',
        'nine':'Девять',
        'ten':'Десять'
        }
    n = 0
    for i in interpreter:
        n =+1
        if i == number:
            print(interpreter[i])
        elif n > 8:
            print(None)


num_translate('one')

# Задание 3
def thesaurus(*names):
    dict_name = {}
    for name in names:
        dict_name[name[0]] = dict_name.get(name[0], []) + [name]
    return print(dict_name)

thesaurus('маша', 'дима', 'оля', 'оксена','мария','диана')




# Задание 5
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

from random import choice

def get_joket(n,flag=True):

    for i in range(n):
        joke =f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
        print (joke)
        list = []
        if flag == True:
            list_2 = joke.split()
            for noun in nouns:
                for fun in list_2:
                    if noun == fun:
                        nouns.remove(noun)

            for adverb in adverbs:
                for fun in list_2:
                    if adverb == fun:
                        adverbs.remove(adverb)

            for adjective in adjectives:
                for fun in list_2:
                    if adjective == fun:
                        adjectives.remove(adjective)

get_joket(2,flag=True)


