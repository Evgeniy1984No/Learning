"""
Конкатенация файлов 🌶️
На вход программе подается натуральное число
�
n и
�
n строк с названиями файлов. Напишите программу, которая создает файл output.txt и выводит в него содержимое всех
файлов, не меняя их порядка. Смотрите Примечание 2 для понимания работы программы.

Формат входных данных
На вход программе подается натуральное число
�
n и
�
n строк названий существующих файлов.

Формат выходных данных
Программа должна создать файл с именем output.txt в соответствии с условием задачи.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

Примечание 2. Если бы на вход было подано
2
2 файла и эти файлы содержали бы строки

Early in the morning
и

we
went
for mushrooms
то результирующий файл output.txt выглядел бы следующим образом:

Early in the morningwe
went
for
mushrooms

----------------------------------------------------------------------------------------------------------------------
Решение можно сделать в 3 строки. Тестовый образец дал преподаватель ниже, но там в комментах, не все заметят, поэтому
дублирую:

Содержимое 1 файла:
Python
c++

Содержимое 2 файла:
c#
php

Результат:
python
c++c#
php
То есть при склейке файлов "\n" не нужно добавлять. На чем лично я погорел :\

Если бы у людей перед глазами был образец выше + больше людей бы использовали IDE для проверки (replit или что-то
другое), то в этом задании было бы не 37% успешных решений, а гораздо больше.

@Дмитрий_Иванов, предлагаю поправочку, чтоб такие, как я, не запарывались здесь. Писать <Содержимое файла 1>,
<Содержимое файла 2> и <Результат> в сам файл не нужно, нужно просто сплошняком в один файл засунуть все строки из
инпут-файлов
"""

for _ in range(int(input())):
    with open('C:/Users/kandz/Downloads/' + input(), encoding='utf-8') as file, \
            open('C:/Users/kandz/Downloads/output.txt', 'a', encoding='utf-8') as output:
        output.writelines(file.readlines())


