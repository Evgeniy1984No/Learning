"""
Упорядоченные дроби
На вход программе подается натуральное число
�
n. Напишите программу, которая выводит в порядке возрастания все несократимые дроби, заключённые между
0
0 и
1
1, знаменатель которых не превосходит
�
n.

Формат входных данных
На вход программе подается натуральное число
�
,
�
>
1
n,n>1.

Формат выходных данных
Программа должна вывести ответ на задачу.

Примечание. Возможно вам потребуется функция gcd(), которая позволяет находить наибольший общий делитель (НОД) двух
чисел. Функция реализована в модуле math.

Тестовые данные 🟢
Sample Input 1:

5
Sample Output 1:

1/5
1/4
1/3
2/5
1/2
3/5
2/3
3/4
4/5
"""
from fractions import Fraction as F
from math import gcd

n = int(input())
res = set()

while n != 1:
    a = n - 1
    for i in range(a, 0, -1):
        if gcd(a, n) == 1 and 0 < F(i, n) < 1:
            res.add(F(i, n))
    n -= 1
print(*sorted(res), sep='\n')
# *********************************************************************************
numbers = set()

for i in range(2, int(input()) + 1):
    for j in range(1, i):
        numbers.add(F(j, i))

print(*sorted(numbers), sep='\n')