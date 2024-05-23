"""
Новый print
Напишите программу с использованием декоратора, которая переопределяет функцию print() так, чтобы она печатала весь
текст в верхнем регистре.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна задекорировать функцию print() так, чтобы она печатала весь текст в верхнем регистре.

Примечание 1. Значения sep и end также должны переводиться в верхний регистр.

Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а
также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print('hi', 'there', end='!')
Sample Output 1:

HI THERE!
Sample Input 2:

print('are you in trouble?')
Sample Output 2:

ARE YOU IN TROUBLE?
Sample Input 3:

print(111, 222, 333, sep='xxx')
Sample Output 3:

111XXX222XXX333
"""


def new_print(func):
    def wrapper(*args, **kwargs):
        modified_args = list(map(str.upper, map(str, args)))
        modified_kwargs = dict(zip(kwargs.keys(), map(str.upper, map(str, kwargs.values()))))
        func(*modified_args, **modified_kwargs)
        return
    return wrapper


# ********************************************************************************************************************
def new_print(func):
    def wrapper(*args, sep=' ', end='\n'):
        func(str(sep).join(map(str, args)).upper(), end = end.upper())
    return wrapper


print = new_print(print)

print(111, 222, 333, sep='e')
