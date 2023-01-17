"""
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по
настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными:
https://stepik.org/media/attachments/lesson/24473/Crimes.csv
"""

import csv

with open('Crimes.csv') as t:
    reader = csv.DictReader(t)
    p_dict = {}
    for row in reader:
        pt = row['Primary Type']
        if '2015' in row['Date']:
            print(row)
            if pt not in p_dict:
                p_dict[pt] = 1
            else:
                p_dict[pt] += 1
    for key, value in p_dict.items():
        if max(p_dict.values()) == value:
            print(key)

