"""
Функция flip_dict()
Рассмотрим следующий словарь:

{'a': [1, 2], 'b': [3, 1], 'c': [2]}
«Перевернем» его, представив ключи в виде значений, а значения — в виде ключей:

{1: ['a', 'b'], 2: ['a', 'c'], 3: ['b']}
Реализуйте функцию flip_dict(), которая принимает один аргумент:

dict_of_lists — словарь, в котором ключом является число или строка, а значением — список чисел или строк
Функция должна возвращать новый словарь (тип defaultdict с типом list в качестве значения по умолчанию), который
представляет собой «перевернутый» словарь dict_of_lists.

Примечание 1. Ключи в возвращаемом функцией словаре, а также элементы в списках должны располагаться в своем исходном
порядке.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию flip_dict(), но не код,
вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))
Sample Output 1:

defaultdict(<class 'list'>, {1: ['a', 'b'], 2: ['a', 'c'], 3: ['b']})
Sample Input 2:

data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'], 'Anri': ['juice', 'coffee']}

for key, values in flip_dict(data).items():
    print(f'{key}: {", ".join(values)}')
Sample Output 2:

cacao: Arthur
tea: Arthur, Timur
juice: Arthur, Timur, Anri
coffee: Timur, Anri
"""
from collections import defaultdict


def flip_dict(dict_of_lists: dict):
    res = defaultdict(list)
    [res[i].append(k) for k, v in dict_of_lists.items() for i in v]
    # for k, v in dict_of_lists.items():
    #     for i in v:
    #         res[i].append(k)
    return res


data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'], 'Anri': ['juice', 'coffee']}

for key, values in flip_dict(data).items():
    print(f'{key}: {", ".join(values)}')

