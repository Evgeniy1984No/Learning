"""
Декоратор do_twice
Реализуйте декоратор do_twice, вызывающий декорируемую функцию два раза.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а
также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор do_twice, но не код,
вызывающий его.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

@do_twice
def beegeek():
    print('beegeek')

beegeek()
Sample Output 1:

beegeek
beegeek
Sample Input 2:

@do_twice
def beegeek():
    print('beegeek')

print(beegeek())
Sample Output 2:

beegeek
beegeek
None
"""


def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


@do_twice
def beegeek():
    print('beegeek')

print(beegeek())

