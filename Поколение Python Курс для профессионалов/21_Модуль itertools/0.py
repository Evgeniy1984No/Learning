# Функция tabulate()
# Реализуйте функцию tabulate(), которая принимает один аргумент:
#
# func — произвольная функция
# Функция tabulate() должна возвращать итератор, генерирующий бесконечную последовательность возвращаемых значений
# функции func сначала с аргументом 1, затем 2, затем 3, и так далее.
#
# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию tabulate(), но не код,
# вызывающий ее.
#
# Примечание 2. Тестовые данные доступны по ссылкам:
#
# Архив с тестами
# GitHub
# Sample Input 1:
#
# func = lambda x: x
# values = tabulate(func)
#
# print(next(values))
# print(next(values))
# Sample Output 1:
#
# 1
# 2
# Sample Input 2:
#
# func = lambda x: x + 10
# values = tabulate(func)
#
# print(next(values))
# print(next(values))
# print(next(values))
# Sample Output 2:
#
# 11
# 12
# 13
from itertools import count


def tabulate(func):
    yield from (func(i) for i in count(1, 1))


func = lambda x: x
values = tabulate(func)

print(next(values))
print(next(values))
print(next(values))