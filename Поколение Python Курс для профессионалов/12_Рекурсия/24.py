"""
Функция get_all_values() 🌶️
Реализуйте функцию get_all_values(), которая принимает два аргумента в следующем порядке:

nested_dicts — словарь, содержащий в качестве значений произвольные объекты или словари, которые, в свою очередь, так
же содержат в качестве значений произвольные объекты или словари; вложенность может быть произвольной
key — хешируемый объект
Функция должна определять все значения, которые соответствуют ключу key в словаре nested_dicts и всех его вложенных
словарях, и возвращать их в виде множества. Если ключа key нет ни в одном словаре, функция должна вернуть пустое
множество.

Примечание 1. Гарантируется, что все искомые значения являются хешируемыми объектами, т.е. могут быть элементами
множества.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_all_values(), но не
код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(*sorted(result))
Sample Output 1:

4 5
Sample Input 2:

my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
result = get_all_values(my_dict, 'hobby')

print(*sorted(result))
Sample Output 2:

math videogames
Sample Input 3:

my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
result = get_all_values(my_dict, 'top_grade')

print(len(sorted(result)))
Sample Output 3:

0
"""


def get_all_values(nested_dicts: dict, key):
    res = set()
    value = nested_dicts.get(key)
    if value is not None:
        res.add(value)
    for elem in nested_dicts.values():
        if isinstance(elem, dict):
            res.update(get_all_values(elem, key))
    return res


my_dict = {
           'Arthur': {'hobby': 'videogames', 'drink': 'cacao'},
           'Timur': {'hobby': 'math'},
           'Dima': {
                   'hobby': 'CS',
                   'sister':
                       {
                         'name': 'Anna',
                         'hobby': 'TV',
                         'age': 14
                       }
                   }
           }

result = get_all_values(my_dict, 'age')
print(*result)