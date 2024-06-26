"""
Ходы коня
На шахматной доске
8
×
8
8×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки, которые бьет конь. Клетку,
где стоит конь, отметьте английской буквой N, клетки, которые бьет конь, отметьте символами *, остальные клетки
заполните точками.

Формат входных данных
На вход программе подаются координаты коня на шахматной доске в шахматной нотации (то есть в виде e4, где сначала
записывается номер столбца (буква от a до h, слева направо), затем номеру строки (цифра от
1
1 до
8
8, снизу вверх)).

Формат выходных данных
Программа должна вывести на экран изображение доски, разделяя элементы пробелами.

Примечание. Шахматная доска имеет вид:



Тестовые данные 🟢
Sample Input 1:

b6
Sample Output 1:

* . * . . . . .
. . . * . . . .
. N . . . . . .
. . . * . . . .
* . * . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
Sample Input 2:

f3
Sample Output 2:

. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . * . * .
. . . * . . . *
. . . . . N . .
. . . * . . . *
. . . . * . * .
"""
desk = [['.'] * 8 for _ in range(8)]
j, i = input()
i = 8 - int(i)
j = ord(j) - 97
desk[i][j] = 'N'
for k in [-2, 2]:
    if i+k in range(8):
        if j+1 in range(8):
            desk[i + k][j + 1] = '*'
        if j-1 in range(8):
            desk[i + k][j - 1] = '*'
    if j+k in range(8):
        if i+1 in range(8):
            desk[i + 1][j + k] = '*'
        if i-1 in range(8):
            desk[i - 1][j + k] = '*'

[print(*row) for row in desk]
"""
_______________________________________________________________________________________________________________________
разница по иксу равна единице и по игреку двойке, либо, наоборот, разница по иксу равна двойке, а по игреку
единице. Это можно заменить равносильным условием произведение разниц равно двойке.
|x-x2|=1 и |y-y2|=2 или |x-x2|=2 и |y-y2|=1 можно заменить на |y - y2| * |x - x2| = 2
"""
x, y = input()
n = 8
board = [['.'] * n for _ in range(n)]
x = ord(x) - 97
y = n - int(y)
board[y][x] = 'N'

for i in range(n):
    for j in range(n):
        if abs(y - i) * abs(x - j) == 2:
            board[i][j] = '*'

for row in board:
    print(*row)