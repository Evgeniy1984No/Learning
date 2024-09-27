# Функция first_largest()
# Реализуйте функцию first_largest(), которая принимает два аргумента в следующем порядке:
#
# iterable — итерируемый объект, элементами которого являются целые числа
# number — произвольное число
# Функция должна возвращать индекс первого элемента итерируемого объекта iterable, который больше number. Если таких
# элементов нет, функция должна вернуть число −1

# Примечание 1. Рассмотрим список чисел

# 10,2,14,7,7,18,20 из первого теста. Первым числом, превосходящим
# 11
# 11, является число
# 14
# 14, которое имеет индекс
# 2
# 2.
#
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
#
# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию first_largest(), но не
# код, вызывающий ее.
#
# Примечание 4. Тестовые данные доступны по ссылкам:
#
# Архив с тестами
# GitHub
# Sample Input 1:
#
# numbers = [10, 2, 14, 7, 7, 18, 20]
#
# print(first_largest(numbers, 11))
# Sample Output 1:
#
# 2
# Sample Input 2:
#
# iterator = iter([-1, -2, -3, -4, -5])
#
# print(first_largest(iterator, 10))
# Sample Output 2:
#
# -1
# Sample Input 3:
#
# iterator = iter([18, 21, 14, 72, 73, 18, 20])
#
# print(first_largest(iterator, 10))
# Sample Output 3:
#
# 0

from itertools import dropwhile, compress, count


def first_largest(iterable, n):
    for i in dropwhile(lambda num: num[1] <= n, enumerate(iterable)):
        return i[0]
    return -1


# ******************************************************************************************************************


best_first_largest = lambda it, n: next(compress(count(), (i > n for i in it)), -1)

iterator = iter([-1, -2, -3, -4, -5])

print(first_largest(iterator, 10))
