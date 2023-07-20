"""
Вам доступен текстовый файл input.txt, состоящий из нескольких строк. Напишите программу для записи содержимого этого
файла в файл output.txt в виде нумерованного списка, где перед каждой строкой стоит ее номер, символ ) и пробел.
Нумерация строк должна начинаться с
1
1.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем output.txt и записать в него пронумерованные строки файла input.txt.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

Примечание 2. Используйте встроенную функцию enumerate().

Примечание 3. Если бы файл input.txt содержал строки:

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
то файл output.txt имел бы вид:

1) Beautiful is better than ugly.
2) Explicit is better than implicit.
3) Simple is better than complex.
4) Complex is better than complicated.
"""
with open('C:/Users/kandz/Downloads/input.txt', encoding='utf-8') as file_in, \
        open('C:/Users/kandz/Downloads/output.txt', 'w', encoding='utf-8') as file_out:
    for num, line in enumerate(file_in.readlines(), 1):
        print(f'{num}) {line.rstrip()}', file=file_out)
