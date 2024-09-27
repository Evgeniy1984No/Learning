# Функция grouper()
# Реализуйте функцию grouper(), которая принимает два аргумента в следующем порядке:
#
# iterable — итерируемый объект
# n — натуральное число
# Функция должна возвращать итератор, генерирующий последовательность, элементами которой являются объединенные в
# кортежи по n элементов соседние элементы итерируемого объекта iterable. Если у элемента не достаточно соседей, то
# ими становится значение None.
#
# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном
# порядке.
#
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
#
# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию grouper(), но не код,
# вызывающий ее.
#
# Примечание 4. Тестовые данные доступны по ссылкам:
#
# Архив с тестами
# GitHub
# Sample Input 1:
#
# numbers = [,1 2, 3, 4, 5, 6]
#
# print(*grouper(numbers, 2))
# Sample Output 1:
#
# (1, 2) (3, 4) (5, 6)
# Sample Input 2:
#
# iterator = iter([1, 2, 3, 4, 5, 6, 7])
#
# print(*grouper(iterator, 3))
# Sample Output 2:
#
# (1, 2, 3) (4, 5, 6) (7, None, None)
# Sample Input 3:
#
# iterator = iter([1, 2, 3])
#
# print(*grouper(iterator, 5))
# Sample Output 3:
#
# (1, 2, 3, None, None)

from itertools import zip_longest, islice, tee, repeat


def grouper(iterable, n):
    # Мое решение:
    # it = tee(iterable, n)
    # groups = [islice(it[i], i, None, n) for i in range(n)]
    # return zip_longest(*groups)
    return zip_longest(*repeat(iter(iterable), n))
    # Пояснение к решению:
    # def grouper(iterable, n):
    #     return repeat(iter(iterable), n)
    # numbers = [1, 2, 3, 4, 5, 6]
    # print(*grouper(numbers, 2))
    # получится что-то вроде <list_iterator object at 0x103036fa0> <list_iterator object at 0x103036fa0>, т.е.
    # кортеж длины n из ссылок на один и тот же итератор, дальше через * раскрываем его, чтобы передать элементы в
    # zip_longest, который будет создавать кортежи, забирая по одному элементу из каждого итератора (а у нас он один и тот
    # же), поэтому и получим требуемое поведение

iterator = iter([1, 2, 3, 4, 5, 6, 7])
print(*grouper(iterator, 3))
