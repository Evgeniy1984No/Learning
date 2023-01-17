"""
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит
на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.

Sample Input:
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15

Sample Output:
Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
"""

table = {}

for count_line in range(int(input())):
    game = [i for i in input().split(';')]
    game[1], game[3] = int(game[1]), int(game[3])
    team_1, team_2 = game[0], game[2]
    goals_1, goals_2 = game[1], game[3]

    for j in game:
        if type(j) == str:
            if j not in table:
                table[j] = [1, 0, 0, 0, 0]
            else:
                table[j][0] += 1

    if goals_1 > goals_2:
        table[team_1][1] += 1
        table[team_1][4] += 3
        table[team_2][3] += 1
    elif goals_1 == goals_2:
        table[team_1][2] += 1
        table[team_2][2] += 1
        table[team_1][4] += 1
        table[team_2][4] += 1
    else:
        table[team_2][1] += 1
        table[team_2][4] += 3
        table[team_1][3] += 1

for key in table:
    print(key, end=':'), print(*table[key])

'''
__________________________________________________________________________________________________________
Оптимальное решение:

def command(c, res):
    if not c in dct: dct[c] = [0, 0, 0, 0, 0]
    dct[c] = [dct[c][0] + 1, 
                dct[c][1] + 1 if res == 3 else dct[c][1],
                dct[c][2] + 1 if res == 1 else dct[c][2],
                dct[c][3] + 1 if res == 0 else dct[c][3],
                dct[c][4] + res,]  
dct = {}
for i in range(int(input())):
    c1, g1, c2, g2 = input().split(';')    
    command(c1, 3 if g1 > g2 else 1 if g1 == g2 else 0)
    command(c2, 3 if g2 > g1 else 1 if g1 == g2 else 0)
for c in dct:
    print('{}:{} {} {} {} {}'.format(c, *dct[c]))

'''


