"""
Класс Knight ♞
Реализуйте класс Knight, описывающий шахматного коня. При создании экземпляра класс должен принимать три аргумента в
следующем порядке:

horizontal — координата коня по горизонтальной оси, представленная латинской буквой от a до h
vertical — координата коня по вертикальной оси, представленная целым числом от 1 до 8 включительно
color — цвет коня (black или white)
Экземпляр класса Knight должен иметь три атрибута:

horizontal — координата коня на шахматной доске по горизонтальной оси
vertical — координата коня на шахматной доске по вертикальной оси
color — цвет коня
Класс Knight должен иметь четыре метода экземпляра:

get_char() — метод, возвращающий символ N
can_move() — метод, принимающий в качестве аргументов координаты клетки по горизонтальной и по вертикальной осям и
возвращающий True, если конь может переместиться на клетку с данными координатами, или False в противном случае
move_to() — метод, принимающий в качестве аргументов координаты клетки по горизонтальной и по вертикальной осям и
заменяющий текущие координаты коня на переданные. Если конь из текущей клетки не может переместиться на клетку с
указанными координатами, его координаты должны остаться неизменными
draw_board() — метод, печатающий шахматное поле, отмечающий на этом поле коня и клетки, на которые может переместиться
конь. Пустые клетки должны быть отображены символом ., конь — символом N, клетки, на которые может переместиться конь,
— символом *
Примечание 1. Шахматное поле имеет вид:



Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

knight = Knight('c', 3, 'white')

print(knight.color, knight.get_char())
print(knight.horizontal, knight.vertical)
Sample Output 1:

white N
c 3
Sample Input 2:

knight = Knight('c', 3, 'white')

print(knight.horizontal, knight.vertical)
print(knight.can_move('e', 5))
print(knight.can_move('e', 4))

knight.move_to('e', 4)
print(knight.horizontal, knight.vertical)
Sample Output 2:

c 3
False
True
e 4
Sample Input 3:

knight = Knight('c', 3, 'white')

knight.draw_board()
Sample Output 3:

........
........
........
.*.*....
*...*...
..N.....
*...*...
.*.*....
"""


class Knight:
    def __init__(self, x, y, color):
        self.horizontal = x
        self.vertical = y
        self.color = color

    def get_char(self):
        return 'N'

    def can_move(self, x_m, y_m):
        x = ord(self.horizontal) - 97
        y = self.vertical
        x_m = ord(x_m) - 97
        # return (abs(x - x_m) == 2 and abs(y - y_m) == 1) or (abs(x - x_m) == 1 and abs(y - y_m) == 2)
        return abs(x - x_m) * abs(y - y_m) == 2

    def move_to(self, x, y):
        if self.can_move(x, y):
            self.horizontal = x
            self.vertical = y

    def draw_board(self):
        board = [['.'] * 8 for _ in range(8)]
        x = ord(self.horizontal) - 97
        y = -self.vertical
        for y2 in range(8, 0, -1):
            for x2 in 'abcdefgh':
                if self.can_move(x2, y2):
                    board[-y2][ord(x2)-97] = '*'
        board[y][x] = 'N'
        for row in board:
            print(*row, sep='')


knight = Knight('c', 3, 'white')

knight.draw_board()
