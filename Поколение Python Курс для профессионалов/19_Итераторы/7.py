"""
Итератор Fibonacci
Реализуйте класс Fibonacci, порождающий итераторы, конструктор которого не принимает никаких аргументов.

Итератор класса Fibonacci должен генерировать бесконечную последовательность чисел Фибоначчи, начиная с
1
1.

Примечание 1. Последовательность Фибоначчи – последовательность натуральных чисел, где каждое последующее число
является суммой двух предыдущих:
1
,
1
,
2
,
3
,
5
,
8
,
13
,
21
,
34
1,1,2,3,5,8,13,21,34

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс Fibonacci.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

fibonacci = Fibonacci()

print(next(fibonacci))
Sample Output 1:

1
Sample Input 2:

fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
Sample Output 2:

1
1
2
3
"""


class MyFibonacci:
    def __init__(self):
        self.first = -1
        self.second = 1
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.first == -1:
            self.first += 1
            return 1
        self.value = self.first + self.second
        self.first = self.second
        self.second = self.value
        return self.value

# *******************************************************************************************************************


class Fibonacci:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a


fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))