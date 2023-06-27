"""
Напишите программу, которая с помощью встроенных функций filter(), map(), sorted() и reduce() выводит в алфавитном
порядке список primary городов с населением более
10
000
000
10000000 человек, в формате:

Cities: Beijing, Buenos Aires, ...
Примечание 1. Тестирующая система никак не "покарает" вас за неиспользование встроенных функций filter(), map(),
sorted() и reduce(), однако лучше сделать это задание честно 😃.

Примечание 2. Ставить запятую в конце вывода не нужно.
"""
from functools import reduce

data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]

primary_filtered = list(filter(lambda elem: elem[0] if elem[1] > 10**7 and elem[2] == 'primary' else None, data))
primary_sorted = list(sorted(map(lambda elem: elem[0], primary_filtered)))
primary = reduce(lambda x, y: x + ', ' + y, primary_sorted[1:], primary_sorted[0])

print(f'Cities: {primary}')