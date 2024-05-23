"""
Декоратор sandwich
Реализуйте декоратор sandwich, который выводит тексты:

---- Верхний ломтик хлеба ----
---- Нижний ломтик хлеба ----
до и после вызова декорируемой функции соответственно.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а
также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор sandwich, но не код,
вызывающий его.


Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

@sandwich
def add_ingredients(ingredients):
    print(' | '.join(ingredients))

add_ingredients(['томат', 'салат', 'сыр', 'бекон'])
Sample Output 1:

---- Верхний ломтик хлеба ----
томат | салат | сыр | бекон
---- Нижний ломтик хлеба ----
Sample Input 2:

@sandwich
def beegeek():
    return 'beegeek'

print(beegeek())
Sample Output 2:

---- Верхний ломтик хлеба ----
---- Нижний ломтик хлеба ----
beegeek
"""


def sandwich(func):
    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        res = func(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return res
    return wrapper


@sandwich
def add_ingredients(ingredients):
    print(' | '.join(ingredients))


add_ingredients(['томат', 'салат', 'сыр', 'бекон'])


@sandwich
def beegeek():
    return 'beegeek'


print(beegeek())