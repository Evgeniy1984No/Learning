"""
Избранные
Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит названия
файлов из этого архива, которые были созданы или изменены позднее 2021-11-30 14:22:00. Названия файлов должны быть
расположены в лексикографическом порядке, каждое на отдельной строке.

Примечание 1. Если файл находится в папке, вывести следует только название без пути.

Примечание 2. Начальная часть ответа выглядит так:

countries.json
data_sample.csv
...
"""
from zipfile import ZipFile
from datetime import datetime

with ZipFile('C:/Users/kandz/Downloads/workbook.zip') as zip_file:
    info = zip_file.infolist()
    t = datetime.fromisoformat('2021-11-30 14:22:00')
    print(type(t))
    favorite = sorted([item.filename.split('/')[-1] for item in info if not item.is_dir() and datetime(*item.date_time) > t])
    print(*favorite, sep='\n')
