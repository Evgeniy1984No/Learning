"""
Популярные домены
Вам доступен файл data.csv, который содержит неповторяющиеся данные о пользователях некоторого ресурса. В первом
столбце записано имя пользователя, во втором — фамилия, в третьем — адрес электронной почты:

first_name,surname,email
John,Wilson,johnwilson@outlook.com
Mary,Wilson,marywilson@list.ru
...
Напишите программу, которая создает файл domain_usage.csv, имеющий следующее содержание:

domain,count
rambler.ru,24
iCloud.com,29
...
где в первом столбце записано название почтового домена, а во втором — количество пользователей, использующих данный
домен. Домены в файле должны быть расположены в порядке возрастания количества их использований, при совпадении
количества использований — в лексикографическом порядке.

Примечание 1. Разделителем в файле data.csv является запятая, при этом кавычки не используются.

Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 3. Начальная часть файла domain_usage.csv выглядит так:

domain,count
rambler.ru,24
iCloud.com,29
...
Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
"""
import csv

with (open('C:/Users/kandz/Downloads/data.csv', encoding='utf-8')) as file_in:
    data = csv.reader(file_in, delimiter=',')
    next(data)
    data_out = dict()
    for row in data:
        domain = row[2][row[2].index('@') + 1:]
        data_out[domain] = data_out.get(domain, 0) + 1

    with (open('C:/Users/kandz/Downloads/domain_usage.csv', 'w', encoding='utf-8', newline='')) as file_out:
        writer = csv.writer(file_out, delimiter=',')
        writer.writerow(['domain', 'count'])
        [writer.writerow(row) for row in sorted(data_out.items(), key=lambda x: (x[1], x[0]))]
