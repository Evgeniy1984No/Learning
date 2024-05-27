"""
Функция primes()
Реализуйте генераторную функцию primes(), которая принимает два аргумента в следующем порядке:

left — натуральное число
right — натуральное число
Функция должна возвращать генератор, порождающий последовательность простых чисел от left до right включительно, а
затем возбуждающий исключение StopIteration.

Примечание 1. Гарантируется, что left <= right.

Примечание 2. Простое число — натуральное число, имеющее ровно два различных натуральных делителя — единицу и самого
себя. Единица простым числом не является.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую генераторную функцию primes(), но не
 код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

generator = primes(1, 15)

print(*generator)
Sample Output 1:

2 3 5 7 11 13
Sample Input 2:

generator = primes(6, 36)

print(next(generator))
print(next(generator))
Sample Output 2:

7
11
"""
from sympy import isprime


def my_primes(left, right):
    d = 2
    for n in range(left, right + 1):
        while n % d != 0 and n != 1:
            d += 1
        if d == n:
            yield n
        d = 2

# ********************************************************************************************************************


def primes(left, right):
    yield from (i for i in range(left, right + 1) if isprime(i))


# ******************************************************************************************************************

def best_primes(left, right):
    left = left if left != 1 else 2
    for n in range(left, right+1):
        if not any(n % i == 0 for i in range(2, n)):
            yield n


generator = best_primes(1, 15)

print(*generator)
