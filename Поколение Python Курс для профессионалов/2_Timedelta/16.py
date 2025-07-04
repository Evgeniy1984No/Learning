"""
Сотрудники организации 😔
Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения. Напишите программу, которая определяет самого молодого сотрудника, празднующего свой день рождения в течение ближайших семи дней от текущей даты.

Формат входных данных
На вход программе в первой строке подается текущая дата в формате DD.MM.YYYY, в следующей строке вводится натуральное
число
�
n — количество сотрудников, работающих в организации. В последующих
�
n строках вводятся данные о каждом сотруднике: имя, фамилия и дата рождения, разделённые пробелом. Дата рождения
указывается в формате DD.MM.YYYY.

Формат выходных данных
Программа должна определить самого молодого сотрудника, празднующего свой день рождения в течение ближайших семи дней,
и вывести его имя и фамилию, разделив пробелом. Если таких сотрудников нет, программа должна вывести текст:

Дни рождения не планируются
Примечание 1. Гарантируется, что у всех сотрудников даты рождения различны.

Примечание 2. Например, для даты 01.11.2021 ближайшими семью днями являются:

02.11.2021, 03.11.2021, 04.11.2021, 05.11.2021, 06.11.2021, 07.11.2021, 08.11.2021
Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

14.11.2021
3
Иван Петров 16.11.1995
Петр Сергеев 14.11.1997
Сергей Романов 17.11.1994
Sample Output 1:

Иван Петров
Sample Input 2:

14.11.2021
3
Иван Петров 25.12.1995
Петр Сергеев 24.11.1997
Сергей Романов 28.12.1994
Sample Output 2:

Дни рождения не планируются
"""
from datetime import datetime, timedelta

pattern = '%d.%m.%Y'

now = datetime.strptime(input(), pattern)
range_check = [(now + timedelta(days=i)).strftime('%d.%m') for i in range(1, 8)]
employees = []
for _ in range(int(input())):
    emp = input().split()
    d = datetime.strptime(emp[2], pattern).strftime('%d.%m')
    if d in range_check:
        employees.append(emp)

if employees:
    younger = max(employees, key=lambda x: datetime.strptime(x[2], pattern))[:2]
else:
    younger = ['Дни рождения не планируются']
print(*younger)

# ****************************************************************************************************************
fmt = '%d.%m.%Y'
date = datetime.strptime(input(), fmt)
emps = [(datetime.strptime(d, fmt), ' '.join(n)) \
        for *n, d in (input().split() for _ in range(int(input())))]
ucbd = [*filter(lambda x: 0 < (x[0].replace(year = date.year) - date).days <= 7, emps)]

print(max(ucbd)[1] if ucbd else 'Дни рождения не планируются')