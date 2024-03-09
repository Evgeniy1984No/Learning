"""
Функция custom_isinstance()
Реализуйте функцию custom_isinstance(), которая принимает два аргумента в следующем порядке:

objects — список произвольных объектов
typeinfo — тип данных или кортеж с типами
Функция должна возвращать единственное число — количество объектов из списка objects, которые принадлежат типу typeinfo
или одному из типов, если был передан кортеж.

Примечание 1. В задаче удобно воспользоваться функцией isinstance().

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию custom_isinstance(), но не
код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, int))
Sample Output 1:

2
Sample Input 2:

numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, (int, float)))
Sample Output 2:

4
Sample Input 3:

numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, list))
Sample Output 3:

0
"""


def custom_isinstance(objects, typeinfo):
    return sum([isinstance(i, typeinfo) for i in objects])


numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, (int, float)))