"""
Вам доступен именованный кортеж Animal, который содержит данные о животном. Первым элементом именованного кортежа
является имя животного, вторым — семейство, третьим — пол, четвертым — цвет. Также доступен файл data.pkl, содержащий
сериализованный список таких кортежей.

Дополните приведенный ниже код, чтобы для каждого кортежа из этого списка он вывел названия его полей и значения этих
полей в следующем формате:

name: <значение>
family: <значение>
sex: <значение>
color: <значение>
Между полями и значениями двух разных кортежей должна располагаться пустая строка.

Примечание 1. Сначала должно следовать содержание первого кортежа из списка, затем второго, и так далее.

Примечание 2. Например, если бы файл data.pkl содержал следующий сериализованный список:

[Animal(name='Alex', family='dogs', sex='m', color='brown'), Animal(name='Nancy', family='dogs', sex='w', color='black')]
то программа должна была бы вывести:

name: Alex
family: dogs
sex: m
color: brown

name: Nancy
family: dogs
sex: w
color: black
"""
from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
with open('C:/Users/kandz/Downloads/data.pkl', 'rb') as file_pkl:
    data_tuples = pickle.load(file_pkl)
    # for tup in data_tuples:
    #     for field, value in zip(Animal._fields, tup):
    #         print(f'{field}: {value}')
    #     print()

    [print(*[f'{f}: {v}' for f, v in animal._asdict().items()], sep='\n', end='\n\n') for animal in data_tuples]
