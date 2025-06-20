"""
Дартс
Будем считать, что игровое поле для игры в дартс представляет собой квадратную матрицу, заполненную натуральными
числами, расположенными в порядке возрастания от краев к центру. Стороной игрового поля будем называть сторону
квадратной матрицы, которую представляет это поле.

Напишите программу, которая создает поле для игры в дартс определенного размера.

Формат входных данных
На вход программе подается единственное натуральное число — сторона игрового поля.

Формат выходных данных
Программа должна создать и вывести игровое поле с заданной стороной.

Примечание 1. Гарантируется, что сторона игрового поля не превышает 18.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

1
Sample Output 1:

1
Sample Input 2:

2
Sample Output 2:

1 1
1 1
Sample Input 3:

3
Sample Output 3:

1 1 1
1 2 1
1 1 1
Sample Input 4:

4
Sample Output 4:

1 1 1 1
1 2 2 1
1 2 2 1
1 1 1 1
Sample Input 5:

5
Sample Output 5:

1 1 1 1 1
1 2 2 2 1
1 2 3 2 1
1 2 2 2 1
1 1 1 1 1
"""
n = int(input())
m = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(i, n - i):
        m[i][j] = m[n - 1 - i][j] = m[j][i] = m[j][n - 1 - i] = i + 1

[print(*[j for j in i]) for i in m]