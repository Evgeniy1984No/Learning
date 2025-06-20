"""
Для игры в бинго требуется карточка размером
5
×
5
5×5, содержащая различные (уникальные) целые числа от
1
1 до
75
75 (включительно), при этом центральная клетка является пустой (она заполняется числом
0
0).

Игра-лото "Cупер Бинго". Играть в лотерею онлайн бесплатно

Напишите программу, которая с помощью модуля random генерирует и выводит случайную карточку для игры в бинго.

Примечание 1. Для наглядности рекомендуем отводить на вывод каждого числа ровно
3
3 символа. Для этого используйте строковый метод ljust().

Примечание 2. Пример возможного ответа:

1  16 31 46 61
10 30 42 47 68
3  18 0  48 63
9  19 34 49 70
5  20 35 50 65
Возможны и другие способы генерации карточки для игры в бинго.
"""
from random import sample

numbers = sample(list(range(1, 76)), 25)
m = [numbers[i:i + 5] for i in range(0, 21, 5)]
m[2][2] = 0

[print(*[str(elem).ljust(3) for elem in row]) for row in m]


"""
______________________________________________________________________________________
"""
numbers = sample(list(range(1, 76)), 25)
bingo = [numbers[i:i + 5] for i in range(0, 21, 5)]
bingo[2][2] = 0

for i in range(5):
    for j in range(5):
        print(str(bingo[i][j]).ljust(3), end=' ')
    print()