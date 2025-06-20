"""
Обмен диагоналей
Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной и побочной
диагонали, при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце нужно поменять местами
элемент на главной диагонали и на побочной диагонали).

Формат входных данных
На вход программе подаётся натуральное число
�
n — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести матрицу с элементами главной и побочной диагонали, поменявшимися своими местами.

Тестовые данные 🟢
Sample Input 1:

3
1 2 3
4 5 6
7 8 9
Sample Output 1:

7 2 9
4 5 6
1 8 3
Sample Input 2:

2
1 2
4 5
Sample Output 2:

4 5
1 2
Sample Input 3:

5
2 2 3 1 3
4 6 6 7 5
7 8 9 7 8
4 5 6 4 5
1 2 3 1 2
Sample Output 3:

1 2 3 1 2
4 5 6 4 5
7 8 9 7 8
4 6 6 7 5
2 2 3 1 3
"""
n = int(input())
matrix = [input().split() for _ in range(n)]
[print(*row) for row in matrix]
print()
for i in range(n//2):
    for j in range(n):
        if i == j or i == n-j-1:
            matrix[i][j], matrix[~i][j] = matrix[~i][j], matrix[i][j]
[print(*row) for row in matrix]
"""
_____________________________________________________________________________________________________________________
"""
n = int(input())
dat = [input().split() for _ in range(n)]
for i in range(n // 2):
    dat[i][i], dat[~i][i] = dat[~i][i], dat[i][i]
    dat[i][~i], dat[~i][~i] = dat[~i][~i], dat[i][~i]
[print(*row) for row in matrix]