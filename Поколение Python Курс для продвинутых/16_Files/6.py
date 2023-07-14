"""
Статистика по файлу
Вам доступен текстовый файл file.txt, набранный латиницей. Напишите программу, которая выводит количество букв
латинского алфавита, слов и строк. Выведите три найденных числа в формате, приведенном в примере.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести три найденных числа в формате, приведенном в примере.

Примечание 1. Если бы файл file.txt содержал строки:

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
то результатом было бы:

Input file contains:
108 letters
20 words
4 lines
Примечание 2. Словом называется последовательность из непробельных символов. Например, строка

abc a21 67pop    qwert bo7ok 83456
содержит
6
6 слов: abc, a21, 67pop, qwert, bo7ok, 83456
"""

with open('C:/Users/kandz/Downloads/file.txt', encoding='utf-8') as file:
    lst = list(map(str.strip, file.readlines()))
    sum_l = 0
    sum_w = len(lst)
    for elem in lst:
        sum_l += sum(map(str.isalpha, elem))
        sum_w += sum(map(str.isspace, elem))
    print(f'Input file contains:\n{sum_l} letters\n{sum_w} words\n{len(lst)} lines')

# *****************************************************************************************************
with open('C:/Users/kandz/Downloads/file.txt', encoding='utf-8') as f:
    txt = f.read()
    print('Input file contains:')
    print(sum(map(str.isalpha, txt)), 'letters')
    print(len(txt.split()), 'words')
    print(txt.count('\n') + 1, 'lines')