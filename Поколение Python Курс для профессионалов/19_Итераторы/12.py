"""
Итератор RandomNumbers
Реализуйте класс RandomNumbers, порождающий итераторы, конструктор которого принимает три аргумента в следующем порядке:

left — целое число
right — целое число
n — натуральное число
Итератор класса RandomNumbers должен генерировать последовательность из n случайных чисел от left до right включительно,
 а затем возбуждать исключение StopIteration.

Примечание 1. Гарантируется, что left <= right.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс RandomNumbers.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

iterator = RandomNumbers(1, 1, 3)

print(next(iterator))
print(next(iterator))
print(next(iterator))
Sample Output 1:

1
1
1
Sample Input 2:

iterator = RandomNumbers(1, 10, 2)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
Sample Output 2:

True
True
"""
from random import choice, randint


class MyRandomNumbers:
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > 0:
            self.n -= 1
            return choice(range(self.left, self.right + 1))
        else:
            raise StopIteration


# ******************************************************************************************************************

class RandomNumbers:
    def __init__(self, left, right, n):
        self.data = (randint(left, right) for _ in range(n))

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.data)


iterator = RandomNumbers(1, 1, 3)

print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))