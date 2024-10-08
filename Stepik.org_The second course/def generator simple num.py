"""
Целое положительное число называется простым, если оно имеет ровно два различных делителя, то есть делится только на
единицу и на само себя.
Например, число 2 является простым, так как делится только на 1 и 2. Также простыми являются, например, числа 3, 5, 31,
и еще бесконечно много чисел.
Число 4, например, не является простым, так как имеет три делителя – 1, 2, 4. Также простым не является число 1, так как
оно имеет ровно один делитель – 1.

Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания, начиная с числа 2.

Пример использования:

print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
"""
import itertools


def primes():
    num = 1
    while True:
        num += 1
        div = 0
        for k in range(2, num):
            if num % k == 0:
                div = 1
                break
        if num == 2 or div == 0:
            yield num


# gen = primes()
# for i in range(12):
#     x = next(gen)
#     print(x)

print(list(itertools.takewhile(lambda x: x <= 120, primes())))

"""
спасибо за формулу Вильсона

не пришлось множить сущности (доп. списки и проч.) :)
"""


def primes():
    i, f = 2, 1  # число и факториал предыдущего числа
    while True:
        if (f + 1) % i == 0:  # проверяем на простоту по теореме Вильсона через факториал
            yield i
        f, i = f * i, i + 1  # сначала пересчитываем факториал для текущего числа, затем увеличиваем число
