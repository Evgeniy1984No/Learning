"""
Возрастание классов 🌶️
Вам доступен файл student_counts.csv, который содержит данные о количестве учеников в некотором учебном заведении за
период
2000
2000 —
2021
2021 г. В первом столбце записан год, в последующих столбцах записан класс и количество учеников в данном классе в этом
году:

year,5-Б,3-Б,8-А,2-Г,7-Б,1-Б,3-Г,3-А,2-В,6-Б,6-А,8-Б,8-Г,11-А,2-А,7-А,5-А,2-Б,10-А,11-Б,8-В,4-А,7-В,3-В,1-А,9-А,11-В
2000,19,15,18,29,19,17,26,29,28,30,26,27,27,22,29,19,27,20,16,18,15,27,19,29,22,20,23
2001,21,30,22,19,26,20,24,27,20,30,24,30,29,21,20,19,29,27,23,25,30,30,23,22,22,18,22
...
Напишите программу, которая записывает данную таблицу в файл sorted_student_counts.csv, располагая все столбцы в порядке
возрастания классов, при совпадении классов — в порядке возрастания букв.

Примечание 1. Каждый класс содержит номер и букву и записывается в следующем формате:

<номер класса>-<буква класса>
Примечание 2. Разделителем в файле student_counts.csv является запятая, при этом кавычки не используются.

Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 4. Начальная часть файла sorted_student_counts.csv выглядит так:

year,1-А,1-Б,2-А,2-Б,...
2000,22,17,29,20,...
2001,22,20,20,27,...
...
Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
"""
import csv

with open('C:/Users/kandz/Downloads/student_counts.csv', encoding='utf-8') as f_input:
    rows = list(csv.DictReader(f_input, delimiter=','))
    d_sorted = []
    for d in rows:
        temp = [list(d.items())[0]]
        temp += sorted(list(d.items())[1:], key=lambda x: (int(x[0].split('-')[0]), x[0].split('-')[1]))
        d_sorted.append(dict(temp))

with open('C:/Users/kandz/Downloads/sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as f_output:
    writer = csv.DictWriter(f_output, fieldnames=d_sorted[0].keys(), delimiter=',')
    writer.writeheader()
    writer.writerows(d_sorted)


# ***********************************************************************************************************************
"""
мы не сортируем объект reader, сортируется лишь список названий столбцов, который после передается writer объекту. 
Элементы reader объекта представлены словарями, ключами в которых являются названия столбцов. При записи значения 
столбцов располагаются в соответствии: ключ словаря — название столбца. 

Например, следующий код:

import csv

data = {'a': 1, 'b': 2, 'c': 3}

with open('data.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=['c', 'b', 'a'])
    writer.writeheader()
    writer.writerow(data)
    
создаст файл data.csv с содержанием: 

c,b,a
3,2,1
"""


def key_func(grade):
    number, letter = grade.split('-')
    return int(number), letter


with open('C:/Users/kandz/Downloads/student_counts.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    columns = ['year'] + sorted(reader.fieldnames[1:], key=key_func)
    rows = list(reader)

with open('C:/Users/kandz/Downloads/sorted_student_counts.csv', 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(rows)

