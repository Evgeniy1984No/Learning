"""
Сумма чисел в файле
Вам доступен текстовый файл nums.txt. В файле могут быть записаны целые неотрицательные числа и все, что угодно. Числом
назовем последовательность одной и более цифр, идущих подряд (число всегда неотрицательно).

Напишите программу, которая вычисляет сумму всех чисел, записанных в файле.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести сумму всех чисел, записанных в файле.

Примечание 1. Если бы файл nums.txt содержал строки:

 123   jhjk
bhjip456qwerty
1x2y3 4 5 6
sfsd 0 dfgfd
10abc20de30pop5 5 5 5
то результатом было бы:

680
"""
with open('C:/Users/kandz/Downloads/nums.txt') as file:
    # lst = file.read()
    # print(lst)
    lst = list(map(str.strip, file.readlines()))
    print(lst)
    nums = list()
    # nums = list(map(lambda x: map(lambda y: )))
    for elem in lst:
        for char in elem:
            if char.isalpha():
                elem = elem.replace(char, ' ')
        nums.append(list(map(int, elem.split())))
    print(sum(map(sum, nums)))
# **********************************************************************************************************************
with open('C:/Users/kandz/Downloads/nums.txt', encoding='utf-8') as file:
    row = ''.join(c if c.isdigit() else ' ' for c in file.read())
    print(sum(map(int, row.split())))