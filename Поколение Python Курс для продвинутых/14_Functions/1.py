"""
Функция ignore_command() принимает на вход один строковый аргумент command – команда, которую нужно проверить,

и возвращает значение True, если в команде содержится подстрока из списка ignore и False – если нет.

def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']

    for word in ignore:
        if word in command:
            return True
    return False
Перепишите функцию ignore_command(), чтобы она использовала встроенные функции all()/any() сохранив при этом ее
функционал.

Примечание 1. Следующий программный код:

print(ignore_command('get ip'))
print(ignore_command('select all'))
print(ignore_command('delete'))
print(ignore_command('trancate'))
должен выводить:

True
True
True
False
"""


def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    return any(map(lambda word: word in command, ignore))


print(ignore_command('get ip'))
print(ignore_command('select all'))
print(ignore_command('delete'))
print(ignore_command('trancate'))