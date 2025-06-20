"""
Сумма дробей 2
На вход программе подается натуральное число n. Напишите программу, которая вычисляет и выводит рациональное число,
равное значению выражения
1/1! + 1/2! + 1/3! + 1/4! + … + 1/n!


Формат входных данных
На вход программе подается натуральное числоn.

Формат выходных данных
Программа должна вывести ответ на задачу.

Примечание 1. Результирующая дробь должна быть несократимой.

Примечание 2. Для вычисления факториала можно использовать функцию factorial из модуля math.
Sample Input 1:

1
Sample Output 1:

1
Sample Input 2:

2
Sample Output 2:

3/2
Sample Input 3:

3
Sample Output 3:

5/3
Sample Input 4:

4
Sample Output 4:

41/24
"""
from fractions import Fraction as F


def fact(f):
    if f == 0:
        return 1
    return fact(f - 1) * f


n = int(input())
res = 0
for i in range(1, n+1):
    res += F(1, fact(i))
print(res)
# ********************************************************************************************************************
"В данной задаче применять функцию факториала на каждой итерации не эффективно."
from fractions import Fraction

n = int(input())

factor = 1
s = 0
for i in range(1, n + 1):
    factor *= i
    s += Fraction(1, factor)

print(s)