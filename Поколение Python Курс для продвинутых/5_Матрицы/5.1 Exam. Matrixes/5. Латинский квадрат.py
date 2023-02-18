"""
Латинский квадрат 🌶️
Латинским квадратом порядка
�
n называется квадратная матрица размером
�
×
�
n×n, каждая строка и каждый столбец которой содержат все числа от
1
1 до
�
n. Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.

Формат входных данных
На вход программе подаётся натуральное число
�
n — количество строк и столбцов в матрице, затем элементы матрицы:
�
n строк, по
�
n чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является латинским квадратом, и слово NO, если не является.

Тестовые данные 🟢
Sample Input 1:

4
2 3 4 1
3 4 1 2
4 1 2 3
1 2 3 4
Sample Output 1:

YES
Sample Input 2:

3
1 2 3
3 2 1
2 3 4
Sample Output 2:

NO
"""
n = int(input())
mat = [[int(i) for i in input().split()] for _ in range(n)]
check = {i for i in range(1, n+1)}
elem_mat = set()
col = []
res = 'YES'
for row in mat:
    elem_mat.update(row)
    if check != elem_mat:
        res = 'NO'
        break
    else:
        elem_mat.clear()
else:
    for i in range(n):
        for j in range(n):
            col.append(mat[j][i])
        elem_mat.update(col)
        if check != elem_mat:
            res = 'NO'
            break
        else:
            elem_mat.clear()
print(res)
"""
_______________________________________________________________________________________
"""
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
numbers = list(range(1, n + 1))
result = 'YES'

for i in range(n):
    row_nums = sorted(matrix[i])
    col_nums = sorted([matrix[j][i] for j in range(n)])
    if row_nums != numbers or col_nums != numbers:
        result = 'NO'
        break
print(result)