"""
Последний день на Титанике
Вам доступен файл titanic.csv, который содержит данные о пассажирах, присутствовавших на борту парохода Титаник.
В первом столбце указана единица, если пассажир выжил, и ноль в противном случае, во втором столбце записано полное имя
пассажира, в третьем — пол, в четвертом — возраст:

survived;name;sex;age
0;Mr. Owen Harris Braund;male;22
1;Mrs. John Bradley (Florence Briggs Thayer) Cumings;female;38
...
Напишите программу, которая выводит имена выживших пассажиров, которым было менее
18
18 лет, каждое на отдельной строке. Причем сначала должны быть расположены имена всех пассажиров мужского пола, а
затем — женского, имена же непосредственно в мужском и женском списках должны быть расположены в своем исходном порядке.

Примечание 1. Разделителем в файле titanic.csv является точка с запятой, при этом кавычки не используются.

Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 3. Часть ответа выглядит так:

Master. Gerios Moubarek
Master. Alden Gates Caldwell
...
Master. Harold Theodor Johnson
Mrs. Nicholas (Adele Achem) Nasser
Miss. Marguerite Rut Sandstrom
...
Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
"""
import csv

with (open('C:/Users/kandz/Downloads/titanic.csv', encoding='utf-8')) as f:
    data = csv.reader(f, delimiter=';')
    next(data)
    lst = list(filter(lambda x: int(x[0]) and float(x[3]) < 18, data))
    [print(i[1]) for i in sorted(lst, key=lambda x: x[2], reverse=True)]
