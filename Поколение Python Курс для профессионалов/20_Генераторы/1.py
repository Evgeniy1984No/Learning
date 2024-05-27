"""
Функция alternating_sequence()
Реализуйте генераторную функцию alternating_sequence(), которая принимает один аргумент:

count — натуральное число, по умолчанию имеет значение None
Если count имеет значение None, функция должна возвращать генератор, порождающий бесконечный знакочередующийся ряд
натуральных чисел.

Если count имеет в качестве значения натуральное число, функция должна возвращать генератор, порождающий первые count
чисел знакочередующегося ряда натуральных чисел, а затем возбуждающий исключение StopIteration.

Примечание 1. Знакочередующийся ряд натуральных чисел имеет вид:
1
,
−
2
,
3
,
−
4
,
5
,
−
6
,
7
,
−
8
,
9
,
−
10
,
.
.
.
1,−2,3,−4,5,−6,7,−8,9,−10,...
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую генераторную  функцию
alternating_sequence(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

generator = alternating_sequence()

print(next(generator))
print(next(generator))
Sample Output 1:

1
-2
Sample Input 2:

generator = alternating_sequence(10)

print(*generator)
Sample Output 2:

1 -2 3 -4 5 -6 7 -8 9 -10
"""


def my_alternating_sequence(count=None):
    n = 0
    while n != count:
        n += 1
        yield n if n % 2 else -n


def alternating_sequence(count=None):
    n = 0
    while n != count:
        n += 1
        sign = [-1, 1][n % 2]
        yield n * sign


generator = alternating_sequence(10)

print(*generator)
