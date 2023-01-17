"""
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана
следующая информация:
Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает его
среднюю оценку по трём предметам на отдельной строке, соответствующей этому абитуриенту, в файл с ответом.
Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и добавьте полученные
значения, разделённые пробелом, последней строкой в файл с ответом.
В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику и одной строкой
со средними оценками по трём предметам.
Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:
print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
"""

import os

input_file = 'Input.txt'
path = os.path.join('D:/', 'Google Drive', 'PycharmProjects', 'Learning', input_file)

average_math = 0
average_phys = 0
average_rus = 0
count = 0

output_file = open('Outpu.txt', 'w')

with open(path) as arr:
    for line in arr:
        line = line.strip().split(';')
        average_of_student = 0
        for i in range(1, len(line)):
            line[i] = int(line[i])
            average_of_student += line[i]
        line.append(average_of_student/(len(line)-1))
        average_math += line[1]
        average_phys += line[2]
        average_rus += line[3]
        count += 1
        print(line)

        output_file.write(str(line[-1]))
        output_file.write('\n')

    avr = str(average_math/count) + ' ' + str(average_phys/count) + ' ' + str(average_rus/count)
    output_file.write(avr)

output_file.close()
'''
s = []
s_1 = []
# читаем данные с файла, пишем в новый список s
with open('In1.txt') as file:
    for i in file:
        s0 = i.strip().split(';')
        s0.remove(s0[0])
        s.append(s0)
#

# считаем индивидуальные средние + пишем в файл (в столбец)
ouf = open('Out1.txt', 'w')
for l in range(len(s)):
    si = [int(k) for k in s[l]]
    ouf.write(str((sum(si) / len(s[l]))) + '\n')
#

# считаем общие средние + пишем в файл (в строку)
for y in range(len(s[0])):
    for z in range(len(s)):
        a = int(s[z][y])
        s_1.append(a)
    ouf.write(str(sum(s_1[0:len(s)]) / len(s)) + ' ')
    del s_1[0:len(s)]
ouf.close()
#
'''