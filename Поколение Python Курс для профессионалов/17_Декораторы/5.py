"""
екоратор takes_positive
Реализуйте декоратор takes_positive, который проверяет, что все аргументы, передаваемые в декорируемую функцию,
являются положительными целыми числами.

Если хотя бы один аргумент не удовлетворяет данному условию, декоратор должен возбуждать исключение:

TypeError, если аргумент не является целым числом
ValueError, если аргумент является целым числом, но отрицательным или равным нулю
Примечание 1. Приоритет возбуждения исключений при несоответствии аргумента обоим условиям или при наличии разных
аргументов, несоответствующих разным условиям: TypeError, затем ValueError.

Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а
также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый декоратор takes_positive, но не
код, вызывающий его.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

@takes_positive
def positive_sum(*args):
    return sum(args)

print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
Sample Output 1:

55
Sample Input 2:

@takes_positive
def positive_sum(*args):
    return sum(args)

try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    print(type(err))
Sample Output 2:

<class 'ValueError'>
Sample Input 3:

@takes_positive
def positive_sum(*args):
    return sum(args)

try:
    print(positive_sum('10', 20, 10))
except Exception as err:
    print(type(err))
Sample Output 3:

<class 'TypeError'>
"""


def takes_positive(func):
    def wrapper(*args, **kwargs):
        if not all(list(isinstance(i, int) for i in args) + list(isinstance(j, int) for j in kwargs.values())):
            raise TypeError
        elif any(list(i <= 0 for i in args) + list(j <= 0 for j in kwargs.values())):
            raise ValueError
        return func(*args, **kwargs)
    return wrapper


@takes_positive
def positive_sum(*args):
    return sum(args)


print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    print(type(err))


@takes_positive
def positive_sum(*args):
    return sum(args)

try:
    print(positive_sum('10', 20, 10))
except Exception as err:
    print(type(err))