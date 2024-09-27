# Функция txt_to_dict()
# Вам доступен файл planets.txt, содержащий информацию о различных планетах. В первых четырех строках указаны характеристики первой планеты, после чего следует пустая строка, затем характеристики второй планеты, и так далее:
#
# Name = Mercury
# Diameter = 4879.4
# Mass = 3.302×10^23
# OrbitalPeriod = 0.241
#
# Name = Venus
# Diameter = 12103.6
# Mass = 4.869×10^24
# OrbitalPeriod = 0.615
#
# ...
# Реализуйте генераторную функцию txt_to_dict(), которая не принимает никаких аргументов.
#
# Функция должна возвращать генератор, порождающий последовательность словарей, каждый из которых содержит информацию об очередной планете из файла planets.txt, а именно ее название, диаметр, массу и орбитальный период. Например:
#
# {'Name': 'Mercury', 'Diameter': '4879.4', 'Mass': '3.302×10^23', 'OrbitalPeriod': '0.241'}
# Примечание 1. Указанный файл доступен по ссылке.
#
# Примечание 2. При открытии файла используйте явное указание кодировки UTF-8.
#
# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию txt_to_dict(), но не код, вызывающий ее.
#
# Примечание 4. Тестовые данные доступны по ссылкам:
#
# Архив с тестами
# GitHub
# Sample Input:
#
# planets = txt_to_dict()
#
# print(next(planets))
# Sample Output:
#
# {'Name': 'Mercury', 'Diameter': '4879.4', 'Mass': '3.302×10^23', 'OrbitalPeriod': '0.241'}


def txt_to_dict():
    with open('planets.txt', encoding='utf-8') as file:
        list_block = (i.strip().split('\n') for i in file.read().split('\n\n'))
        dicts = (dict(elem.split(' = ') for elem in i) for i in list_block)
        yield from dicts




planets = txt_to_dict()
# print(planets)
# print(next(planets))
# print(next(planets))
# print(next(planets))
# print(next(planets))
# print(next(planets))
# print(next(planets))
# print(next(planets))
# print(next(planets))
# print(next(planets))
# print(type(next(planets)))
print(*planets)
