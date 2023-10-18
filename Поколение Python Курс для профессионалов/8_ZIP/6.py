"""
Шахматы были лучше 🌶️
Вам доступен архив data.zip, содержащий различные папки и файлы. Среди них есть несколько JSON файлов, каждый из которых
содержит информацию о каком-либо футболисте:

{
   "first_name": "Gary",
   "last_name": "Cahill",
   "team": "Chelsea",
   "position": "Defender"
}
У футболиста имеются следующие атрибуты:

first_name — имя
last_name — фамилия
team — название футбольного клуба
position — игровая позиция
Напишите программу, которая обрабатывает только данные JSON файлы и выводит имена и фамилии футболистов, выступающих за
футбольный клуб Arsenal. Футболисты должны быть расположены в лексикографическом порядке имен, а при совпадении — в
лексикографическом порядке фамилий, каждый на отдельной строке.

Примечание 1. Обратите внимание, что наличие у файла расширения .json не гарантирует, что он является корректным
текстовым файлом в формате JSON. Для того чтобы определить, является ли файл корректным текстовым файлом в формате JSON,
воспользуйтесь конструкцией try-except и функцией is_correct_json() из предыдущего урока.

Примечание 2. Начальная часть ответа выглядит так:

Alex Iwobi
Alexis Sanchez
...
"""
from zipfile import ZipFile
import json


def is_correct_json(zip_f, string: str):
    try:
        with zip_f.open(string) as file:
            data = json.loads(file.read().decode('utf-8', 'ignore'))
            if data['team'] == 'Arsenal':
                return data['first_name'], data['last_name']
    except:
        return


with ZipFile('C:/Users/kandz/Downloads/data.zip') as zf:
    info = zf.infolist()
    footballers = []
    for item in info:
        f = is_correct_json(zf, item.filename)
        if f is not None:
            footballers.append(f)
    [print(*i) for i in sorted(footballers) if i is not None]
