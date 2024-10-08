"""
Длинные строки
Вам доступен текстовый файл lines.txt, в котором записаны строки текста. Напишите программу, которая выводит все строки
наибольшей длины из файла, не меняя их порядок.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести строки указанного файла, имеющие наибольшую длину, не меняя их порядка.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Используйте менеджер контекста 🙂.

Примечание 3. Если бы файл lines.txt содержал строки:

One
Twenty one
Two
Twenty two
Three
Twenty thr
то результатом будет:

Twenty one
Twenty two
"""
with open('C:/Users/kandz/Downloads/lines.txt') as file:
    lst = sorted(map(str.strip, file.readlines()), key=lambda x: len(x), reverse=True)
    [print(i) for i in lst if len(i) >= len(lst[0])]

# *********************************************************************************************************************
"""
Решение одним проходом. Да, код не выглядит так аттрактивно, но если вам попадётся очень большой файл, то весь его 
считать в память компьютера не получится, и обходить данные по несколько раз тоже будет накладно по времени.
"""
with open('C:/Users/kandz/Downloads/lines.txt') as f:
    max_len, longest = 0, []
    for line in f:
        line = line.rstrip('\n')
        line_len = len(line)
        if line_len == max_len:
            longest.append(line)
        elif line_len > max_len:
            max_len, longest = line_len, [line]

print('\n'.join(longest))