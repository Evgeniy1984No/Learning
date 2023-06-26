"""
Значение многочлена 🌶️
Многочленом степени n называется выражение вида
  An * x**n + An-1 * x**n-1 + ... + A2 * x**2 + A1 * x + A0
  An, An-1, ..., A2,A1,A0— коэффициенты многочлена (A≠0)

На вход программе на первой строке подаются коэффициенты многочлена, разделенные символом пробела и целое число
�
x на второй строке. Напишите программу, которая вычисляет значение указанного многочлена при заданном значении
�
x.

Формат входных данных
На вход программе на первой строке подаются коэффициенты многочлена (целые числа), разделенные символом пробела и целое число
�
x на второй строке.

Формат выходных данных
Программа должна вывести одно число — значение указанного многочлена при заданном значении
�
x.

Примечание 1. Первый тест задает многочлен
2
�
2
+
4
�
+
3
2x
2
 +4x+3, второй тест задает многочлен
�
6
+
2
�
5
+
3
�
4
+
4
�
3
+
5
�
2
+
6
�
+
7
x
6
 +2x
5
 +3x
4
 +4x
3
 +5x
2
 +6x+7.

Примечание 2. Решение задачи необходимо оформить в виде функции evaluate(coefficients, x), которая принимает список к
оэффициентов и значение аргумента. Функция evaluate() должна быть реализована на основе встроенных функций map() и reduce().

Примечание 3. Не забудьте вызвать функцию evaluate(), чтобы вывести результат 😀.

Тестовые данные 🟢
Sample Input 1:

2 4 3
10
Sample Output 1:

243
Sample Input 2:

1 2 3 4 5 6 7
1
Sample Output 2:

28
Sample Input 3:

-2 4 5
3
Sample Output 3:

-1
Sample Input 4:

10
2
Sample Output 4:

10
Sample Input 5:

3 19
10
Sample Output 5:

49
"""
from functools import reduce


def evaluate(*coefficients, x):
    lst_index = [i for i, v in enumerate(coefficients)]
    # poly = reduce(lambda a, b: a+b, list(map(lambda coef, ind: coef * x**ind, coefficients, lst_index[::-1])))
    return reduce(lambda a, b: a+b, list(map(lambda coef, ind: coef * x**ind, coefficients, lst_index[::-1])))


coefs = [int(i) for i in input().split()]
print(evaluate(*coefs, x=int(input())))
