"""
Бассейны
Тимур планирует пойти в бассейн. Среди всех бассейнов ему подходят те, которые открыты в понедельник в период с 10:00
до 12:00. Также ему нравится плавать по длинным дорожкам, поэтому из всех работающих в это время бассейнов нужно выбрать
бассейн с наибольшей длиной дорожки, при равных значениях — c наибольшей шириной.

Вам доступен файл pools.json, содержащий список JSON-объектов, которые представляют данные о крытых плавательных
бассейнах:

[
   {
      "ObjectName": "Физкультурно-оздоровительный комплекс с бассейном «ГБУ «СШОР № 82» Москомспорта»",
      "AdmArea": "Северо-Восточный административный округ",
      "District": "Алтуфьевский район",
      "Address": "Инженерная улица, дом 5, корпус 1",
      "WorkingHoursSummer": {
         "Понедельник": "10:00-11:00",
         "Вторник": "10:00-11:00",
         "Среда": "10:00-11:00",
         "Четверг": "10:00-11:00",
         "Пятница": "10:00-11:00",
         "Суббота": "10:00-11:00",
         "Воскресенье": "09:00-15:00",
      },
      "DimensionsSummer": {
         "Square": 350,
         "Length": 25,
         "Width": 14,
         "Depth": 1.8
      }
   },
   ...
]
Под «бассейном» будем подразумевать один JSON-объект из этого списка. У бассейна имеются следующие атрибуты:

ObjectName — название, будь то фитнес клуб или спортивный комплекс
AdmArea — административный округ
District — название района
Address — адрес
WorkingHoursSummer — график работы, время начала и закрытия указываются в формате HH:MM
DimensionsSummer — размеры бассейна, где Square — площадь, Length — длина, Width — ширина, Depth — глубина
Напишите программу, которая определяет бассейн, подходящий Тимуру. Программа должна вывести его размеры и адрес в
следующем формате:

<длина>x<ширина>
<адрес>
Примечание 1. Пример вывода:

25x16
Писцовая улица, дом 12, строение 1
Примечание 2. Бассейн должен быть открыт во время всего периода с 10:00 до 12:00. Например, если бассейн работает в
10:00, но не работает в 11:30, он не подходит.

Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
"""
import json
from datetime import datetime

with open('C:/Users/kandz/Downloads/pools.json', encoding='utf-8') as f1:
    pools = json.load(f1)
    conditions = ["Понедельник", "Length", "Width"]
    out = []
    for pool in pools:
        t1 = datetime.strptime(pool["WorkingHoursSummer"][conditions[0]][:5], '%H:%M')
        t2 = datetime.strptime(pool["WorkingHoursSummer"][conditions[0]][6:], '%H:%M')
        if t1 <= datetime.strptime("10:00", '%H:%M') and t2 >= datetime.strptime("12:00", '%H:%M'):
            out.append((pool["DimensionsSummer"]["Length"], pool["DimensionsSummer"]["Width"], pool["Address"]))
    print("{0[0]}x{0[1]}\n{0[2]}".format(max(out, key=lambda x: (x[0], x[1]))))


# ******************************************************************************************************************
def best_pool(data: dict):
    monday_time = data["WorkingHoursSummer"]["Понедельник"].split("-")
    start, finish = [int(time.split(":")[0]) for time in monday_time]
    time = True if start <= 10 and finish >= 12 else False
    dimensions = data["DimensionsSummer"]

    return time, dimensions["Length"], dimensions["Width"]


with open("C:/Users/kandz/Downloads/pools.json", "r", encoding="utf-8") as input_file:
    input_data = json.load(input_file)

    choice = max(input_data, key=best_pool)
    print(f'{choice["DimensionsSummer"]["Length"]}x{choice["DimensionsSummer"]["Width"]}')
    print(choice["Address"])
