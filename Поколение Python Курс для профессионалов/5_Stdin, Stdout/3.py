"""
Урок статистики
Дан список чисел, каждое из которых — рост очередного ученика онлайн-школы BEEGEEK. Напишите программу, которая
определяет рост самого низкого и самого высокого учеников, а также средний рост среди всех учеников.

Формат входных данных
На вход программе подается произвольное количество строк, в каждой строке записано натуральное число — рост очередного
ученика онлайн-школы BEEGEEK.

Формат выходных данных
Программа должна определить рост самого низкого и самого высокого учеников, а также средний рост среди всех учеников.

Полученные результаты должны быть выведены в следующем формате:

Рост самого низкого ученика: <рост самого низкого ученика>
Рост самого высокого ученика: <рост самого высокого ученика>
Средний рост: <средний рост среди всех учеников>
Примечание 1. Если на вход программе ничего не подается, то она должна выводить текст нет учеников.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

185
170
190
155
175
Sample Output 1:

Рост самого низкого ученика: 155
Рост самого высокого ученика: 190
Средний рост: 175.0
Sample Input 2:

Sample Output 2:

нет учеников
"""
import sys

data = [int(i) for i in sys.stdin]

if data:
    print(f'Рост самого низкого ученика: {min(data)}\n'
          f'Рост самого высокого ученика: {max(data)}\n'
          f'Средний рост: {sum(data) / len(data)}')
else:
    print('нет учеников')

# ***************************************************************************************************************
numbers = [int(i) for i in sys.stdin]
try:
    print(f'Рост самого низкого ученика: {min(numbers)}')
    print(f'Рост самого высокого ученика: {max(numbers)}')
    print(f'Средний рост: {sum(numbers) // len(numbers)}')
except:
    print('нет учеников')
