"""
Напишите функцию info_kwargs(), которая принимает произвольное количество именованных аргументов и печатает именованные
аргументы в соответствии с образцом: <имя аргумента>: <значение аргумента>, при этом имена аргументов следуют в
алфавитном порядке (по возрастанию).

Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество именованных
аргументов.

Примечание 2. Следующий программный код:

info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
должен выводить:

age: 28
first_name: Timur
job: teacher
last_name: Guev
"""


def info_kwargs(**kwargs):
    # for key in sorted(kwargs):
    #     print(f'{key}: {kwargs[key]}')
    for k, v in sorted(kwargs.items()):
        print(f'{k}: {v}')



info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')