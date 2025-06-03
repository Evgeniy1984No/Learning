"""
Класс Formatter
Реализуйте класс Formatter. При создании экземпляра класс не должен принимать никаких аргументов.

Класс Formatter должен иметь один статический метод:

format() — метод, принимающий в качестве аргумента объект типа int, float, tuple, list или dict и выводящий информацию
о переданном объекте в формате, зависящем от его типа. Если переданный объект принадлежит какому-либо другому типу,
должно быть возбуждено исключение TypeError с текстом:
Аргумент переданного типа не поддерживается
Примечание 1. Примеры форматирования объектов всех типов показаны в тестовых данных.

Примечание 2. Обратите внимание, что метод format() должен обрамлять апострофами строковые элементы коллекций.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса Formatter нет, она может быть произвольной.

Примечание 5. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

Formatter.format(1337)
Formatter.format(20.77)
Sample Output 1:

Целое число: 1337
Вещественное число: 20.77
Sample Input 2:

Formatter.format([10, 20, 30, 40, 50])
Formatter.format(([1, 3], [2, 4, 6]))
Sample Output 2:

Элементы списка: 10, 20, 30, 40, 50
Элементы кортежа: [1, 3], [2, 4, 6]
Sample Input 3:

Formatter.format({'Cuphead': 1, 'Mugman': 3})
Formatter.format({1: 'one', 2: 'two'})
Formatter.format({1: True, 0: False})
Sample Output 3:

Пары словаря: ('Cuphead', 1), ('Mugman', 3)
Пары словаря: (1, 'one'), (2, 'two')
Пары словаря: (1, True), (0, False)
Sample Input 4:

try:
    Formatter.format('All them years, Dutch, for this snake?')
except TypeError as e:
    print(e)
Sample Output 4:

Аргумент переданного типа не поддерживается
"""
from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')


    @format.register(int)
    def int_format(data):
        print(f'Целое число: {data}')

    @format.register(float)
    def float_format(data):
        print(f'Вещественное число: {data}')

    @format.register(tuple)
    def tuple_format(data):
        print(f'Элементы кортежа: {', '.join(map(str, data))}')

    @format.register(list)
    def list_format(data):
        print(f'Элементы списка: {', '.join(map(str, data))}')

    @format.register(dict)
    def dict_format(data):
        s = [(k, v) for k, v in data.items()]
        print(f'Пары словаря: {', '.join(map(str, s))}')


data = {'Cuphead': 1, 'Mugman': 3}
p = [(k, v) for k, v in data.items()]
print(', '.join(map(str, p)))