"""
Напишите функцию count_args(), которая принимает произвольное количество аргументов и возвращает количество переданных
в нее аргументов.

Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество аргументов.

Примечание 2. Следующий программный код:

print(count_args())
print(count_args(10))
print(count_args('stepik', 'beegeek'))
print(count_args([], (''), 'a', 12, False))
должен выводить:

0
1
2
5
"""


def count_args(*args):
    return len(args)


print(count_args())
print(count_args(10))
print(count_args('stepik', 'beegeek'))
print(count_args([], (''), 'a', 12, False))