"""
Random name and surname
Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.

Напишите программу, которая c помощью модуля random создает
3
3 случайные пары имя + фамилия, а затем выводит их, каждую на отдельной строке.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести текст в формате, приведенном в примере.

Примечание 1. Если бы файлы first_names.txt и last_names.txt содержали строки:

Aaron
Abdul
Abe
Abel
Abraham
Albert
и

Abramson
Adamson
Adderiy
Addington
Adrian
Albertson
Einstein
то результатом могло быть:

Abdul Albertson
Abel Adamson
Albert Einstein
"""
import random

with open('C:/Users/kandz/Downloads/first_names.txt', encoding='utf-8') as first, \
        open('C:/Users/kandz/Downloads/last_names.txt', encoding='utf-8') as last:
        lst_first = list(map(str.strip, first.readlines()))
        lst_last = list(map(str.strip, last.readlines()))
        [print(random.choice(lst_first), random.choice(lst_last)) for _ in range(3)]

# *****************************************************************************************************
with open('C:/Users/kandz/Downloads/first_names.txt', encoding='utf-8') as f, \
        open('C:/Users/kandz/Downloads/last_names.txt', encoding='utf-8') as l:
    z, x = f.readlines(), l.readlines()
    for i in range(3):
        print(random.choice(z).strip(), random.choice(x).strip(), sep=' ')