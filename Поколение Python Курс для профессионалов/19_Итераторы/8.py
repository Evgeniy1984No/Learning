"""
тератор PowerOf
Реализуйте класс PowerOf, порождающий итераторы, конструктор которого принимает один аргумент:

number — ненулевое число
Итератор класса PowerOf должен генерировать бесконечную последовательность целых неотрицательных степеней числа number
в порядке возрастания, начиная с нулевой степени.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимый класс PowerOf.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input:

power_of_two = PowerOf(2)

print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
Sample Output:

1
2
4
8
"""


class PowerOf:
    def __init__(self, number):
        self.number = number
        self.degree = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.degree += 1
        return self.number ** self.degree


power_of_two = PowerOf(2)

print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))