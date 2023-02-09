"""
Магический квадрат 🌶️
Магическим квадратом порядка
�
n называется квадратная таблица размера
�
×
�
n×n, составленная из всех чисел
1
,
2
,
3
,
…
,
�
2
1,2,3,…,n
2
  так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу,
  которая проверяет, является ли заданная квадратная матрица магическим квадратом.

Формат входных данных
На вход программе подаётся натуральное число
�
n — количество строк и столбцов в матрице, затем элементы матрицы:
�
n строк, по
�
n чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.

Тестовые данные 🟢
Sample Input 1:

3
8 1 6
3 5 7
4 9 2
Sample Output 1:

YES
Sample Input 2:

3
8 2 6
3 5 7
4 9 1
Sample Output 2:

NO
Sample Input 3:

3
4 9 2
3 5 7
8 1 6
Sample Output 3:

YES
"""
n = int(input())
mat = [[int(i) for i in input().split()] for _ in range(n)]
print(mat)
q = {i for i in range(1, n*n+1)}
m = set()
s = sum(mat[0])
diag_m = []
diag_s = []
res = 'YES'

print(q)
for row in mat:
    m.update(row)
print(m)
if q != m:
    res = 'NO'
else:
    for row in mat:
        if sum(row) != s:
            res = 'NO'
            break
    else:
        for r in range(n):
            col = []
            diag_m.append(mat[r][r])
            diag_s.append(mat[r][n-r-1])
            for c in range(n):
                col.append(mat[c][r])
            if sum(col) != s:
                res = 'NO'
                break
        if sum(diag_s) != s or sum(diag_m) != s:
            res = 'NO'

print(res)