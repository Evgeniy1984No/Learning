"""
Функция pluck()
Реализуйте функцию pluck(), которая принимает три аргумента в следующем порядке:

data — словарь произвольной вложенности
path — строка, представляющая собой ключ или последовательность ключей, перечисленных через точку .
default — произвольный объект, значение по умолчанию; имеет значение None, если не передан явно
Функция должна возвращать значение по ключу path из словаря data. Если path представляет собой последовательность
ключей, например, key1.key2, то возвращаемым значением функции должно быть значение по ключу key2 из словаря data[key1].
Если указанного ключа или хотя бы одного ключа из последовательности ключей в словаре нет, функция должна вернуть
значение default.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию pluck(), но не код,
вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}

print(pluck(d, 'x'))
Sample Output 1:

40
Sample Input 2:

d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}

print(pluck(d, 'a.b'))
Sample Output 2:

5
Sample Input 3:

d = {'a': {'b': {'c': {'d': {'e': 4}}}}}

print(pluck(d, 'a.b.c'))
Sample Output 3:

{'d': {'e': 4}}
"""


def pluck(data, path, default=None):
    for key in path.split('.'):
        data = data.get(key, default)
    return data


d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}

print(pluck(d, 'z', 0))