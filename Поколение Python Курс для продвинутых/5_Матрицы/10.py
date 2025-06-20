"""
Симметричная матрица
Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.

Формат входных данных
На вход программе подаётся натуральное число
�
n — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести YES, если матрица симметрична относительно главной диагонали, и слово NO в противном случае.

Тестовые данные 🟢
Sample Input 1:

3
0 1 2
1 2 3
2 3 4
Sample Output 1:

YES
Sample Input 2:

3
0 1 2
1 2 7
2 3 4
Sample Output 2:

NO
Sample Input 3:

2
1 2
3 4
Sample Output 3:

NO
"""
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
matrix_t = []
for i in range(n):
    row_t = []
    for j in range(n):
        row_t.append(matrix[j][i])
    matrix_t.append(row_t)
if matrix == matrix_t:
    print("YES")
else:
    print("NO")

"""
____________________________________________________________________________________________________________________
"""
n = int(input())
matrix = [input().split() for _ in range(n)]
result = 'YES'

for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            result = 'NO'
            break
    if result == 'NO':
        break

print(result)