"""
Функция palindromes()
Реализуйте генераторную функцию palindromes(), которая не принимает никаких аргументов.

Функция должна возвращать генератор, порождающий бесконечную последовательность натуральных чисел-палиндромов.

Примечание 1. Число-палиндром — число, которое читается одинаково как справа налево, так и слева направо.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую генераторную функцию palindromes(),
но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

generator = palindromes()

print(next(generator))
print(next(generator))
print(next(generator))
Sample Output 1:

1
2
3
Sample Input 2:

generator = palindromes()
numbers = [next(generator) for _ in range(30)]

print(*numbers)
Sample Output 2:

1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101 111 121 131 141 151 161 171 181 191 202 212
"""


def palindromes():
    yield from range(1, 10)
    n = 11
    while True:
        if str(n) == str(n)[::-1]:
            yield n
        n += 1
# *********************************************************************************************************************
# THE BEST SOLUTION -->
#       -->yield from (i for i, _ in enumerate(iter(bool, True), 1) if str(i) == str(i)[::-1]) <--
# Если функции iter() передается два аргумента, то первый аргумент callable должен являться функцией, а второй аргумент
# sentinel — некоторым стоп-значением. В этом случае, созданный итератор будет вызывать указанную функцию callable и
# проверять полученное значение на равенство со значением sentinel. Если полученное значение равно sentinel, то
# возбуждается исключение StopIteration, иначе итератор выдает значение, полученное из функции callable.
#
# Например, с помощью функции iter() мы можем создать бесконечный итератор, генерирующий единственное значение — 0
# Приведенный ниже код:
# zero_iterator = iter(int, -1)
#
# for i in range(5):
#     print(next(zero_iterator))
#
# print(type(zero_iterator))


generator = palindromes()

for _ in range(10_000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
