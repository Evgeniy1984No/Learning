"""
Функция custom_sort() 🌶️
Реализуйте функцию custom_sort(), которая принимает два аргумента в следующем порядке:

ordered_dict — словарь OrderedDict
by_values — булево значение, по умолчанию имеет значение False
Функция должна сортировать словарь ordered_dict:

по ключам, если by_values имеет значение False
по значениям, если by_values имеет значение True
Примечание 1. Функция должна изменять переданный словарь, а не возвращать новый. Возвращаемым значением функции должно
быть None.

Примечание 2. Гарантируется, что переданный в функцию словарь можно отсортировать, то есть он не содержит ключи,
имеющие разные типы, а также значения, имеющие разные типы.

Примечание 3. Если два элемента имеют равные значения, то следует сохранить их исходный порядок следования.

Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимую функцию custom_sort(), но не код,
вызывающий ее.

Примечание 5. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)

print(data)
Sample Output 1:

OrderedDict([('Anabel', 17), ('Brian', 40), ('Carol', 16), ('Dustin', 29)])
Sample Input 2:

data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data, by_values=True)

print(*data.items())
Sample Output 2:

('Mercury', 1) ('Venus', 2) ('Earth', 3) ('Mars', 4)
"""
from collections import OrderedDict


def custom_sort(ordered_dict: OrderedDict, by_values=False) -> None:
    keys_sorted = sorted(ordered_dict.items(), key=lambda x: x[by_values])
    [ordered_dict.move_to_end(k[0]) for k in keys_sorted]


data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data, by_values=True)

print(*data.items())