"""
Шахматная доска
На вход программе подаются два натуральных числа
�
n и
�
m. Напишите программу для создания матрицы размером
�
×
�
n×m, заполнив её символами . и * в шахматном порядке. В левом верхнем углу должна стоять точка. Выведите полученную
матрицу на экран, разделяя элементы пробелами.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа
�
n и
�
m — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу, описанную в условии задачи.

Тестовые данные 🟢
Sample Input 1:

3 4
Sample Output 1:

. * . *
* . * .
. * . *
Sample Input 2:

2 2
Sample Output 2:

. *
* .
Sample Input 3:

1 8
Sample Output 3:

. * . * . * . *
"""
n, m = [int(i) for i in input().split()]
desk = [['.'] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if (i == 0 or i % 2 == 0) and (j % 2 != 0):
            desk[i][j] = '*'
        if i % 2 != 0 and (j == 0 or j % 2 == 0):
            desk[i][j] = '*'
    print(*desk[i])
"""
_____________________________________________________________________________________________________________________
"""
n, m = [int(i) for i in input().split()]
board = [['.'] * m for _ in range(n)]

for i in range(n):
    for j in range(1 - i % 2, m, 2):
        board[i][j] = '*'

for row in board:
    print(*row)
