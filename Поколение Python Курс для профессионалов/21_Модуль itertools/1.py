# ункция factorials()
# Реализуйте функцию factorials() с использованием функции accumulate(), которая принимает один аргумент:
#
# n — натуральное число
# Функция должна возвращать итератор, генерирующий последовательность из n чисел, каждое из которых является факториалом
# очередного натурального числа.
#
# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию factorials(), но не код,
# вызывающий ее.
#
# Примечание 2. Тестовые данные доступны по ссылкам:
#
# Архив с тестами
# GitHub
# Sample Input 1:
#
# numbers = factorials(6)
#
# print(*numbers)
# Sample Output 1:
#
# 1 2 6 24 120 720
# Sample Input 2:
#
# numbers = factorials(2)
#
# print(next(numbers))
# print(next(numbers))
# Sample Output 2:
#
# 1
# 2
import itertools as it


def factorials(n):
    yield from it.accumulate(range(1, n+1), lambda x, y: x * y)


numbers = factorials(2)

print(*numbers)