"""
Декоратор repeat
Реализуйте декоратор repeat, который принимает один аргумент:

times — натуральное число
Декоратор должен вызывать декорируемую функцию times раз.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а
также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор repeat, но не код,
вызывающий его.

Примечание 3. Тестовые данные доступны по по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

@repeat(3)
def say_beegeek():
    '''documentation'''
    print('beegeek')

say_beegeek()
Sample Output 1:

beegeek
beegeek
beegeek
Sample Input 2:

@repeat(4)
def say_beegeek():
    '''documentation'''
    print('beegeek')

print(say_beegeek.__name__)
print(say_beegeek.__doc__)
Sample Output 2:

say_beegeek
documentation
"""
import functools


def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                v = func(*args, **kwargs)
            return v
        return wrapper
    return decorator



@repeat(4)
def say_beegeek():
    '''documentation'''
    print('beegeek')

print(say_beegeek.__name__)
print(say_beegeek.__doc__)