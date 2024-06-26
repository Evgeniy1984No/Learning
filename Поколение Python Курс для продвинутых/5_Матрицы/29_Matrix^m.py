"""
Возведение матрицы в степень 🌶️
Напишите программу, которая возводит квадратную матрицу в
�
m-ую степень.

Формат входных данных
На вход программе подаётся натуральное число
�
n — количество строк и столбцов в матрице, затем элементы матрицы, затем натуральное число
�
m.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

Тестовые данные 🟢
Sample Input 1:

3
1 2 3
4 5 6
7 8 9
2
Sample Output 1:

30 36 42
66 81 96
102 126 150
Sample Input 2:

3
1 2 1
3 3 3
1 2 1
5
Sample Output 2:

1666 2222 1666
3333 4443 3333
1666 2222 1666
Sample Input 3:

5
1 2 1 1 2
3 3 3 3 3
1 2 1 1 2
3 3 3 3 3
1 2 1 1 2
3
Sample Output 3:

133 176 133 133 176
279 369 279 279 369
133 176 133 133 176
279 369 279 279 369
133 176 133 133 176
"""
n = int(input())
a = [[int(i) for i in input().split()] for _ in range(n)]

b = []
[b.append(i) for i in a]
print()

c = [[0] * n for _ in range(n)]
m = int(input())
for k in range(m-1):
    for ci in range(n):
        for cj in range(n):
            for j in range(n):
                c[ci][cj] += a[ci][j] * b[j][cj]
    a = c
    c = [[0] * n for _ in range(n)]

[print(*[str(j) for j in i]) for i in a]
