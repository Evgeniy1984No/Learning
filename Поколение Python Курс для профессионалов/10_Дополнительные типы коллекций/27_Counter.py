"""
Бесплатные курсы берут свое 😢
Для дополнительного заработка Тимур решил заняться продажей овощей. У него имеются данные о продажах за год, разделенные
на четыре файла по кварталам: quarter1.csv, quarter2.csv, quarter3.csv и quarter4.csv. В каждом файле в первом столбце
указывается название продукта, а в последующих — количество проданного продукта в килограммах за определенный месяц:

продукт,январь,февраль,март
Картофель,39,61,3
Дайкон,51,96,83
...
Также присутствует файл prices.json, содержащий словарь, в котором ключом является название продукта, а значением —
цена за килограмм в рублях:

{
   "Картофель": 53,
   "Дайкон": 55,
...
}
Напишите программу, которая выводит единственное число — сумму, заработанную Тимуром за год на продаже овощей.

Примечание 1. Ссылки на указанные файлы: quarter1.csv, quarter2.csv, quarter3.csv, quarter4.csv, prices.json. Ответ на
задачу доступен по ссылке.

Примечание 2. При открытии файла используйте явное указание кодировки UTF-8.

"""
import csv
import json
from collections import Counter


def total_profit(file: str, prices: json):
    with open("C:/Users/kandz/Downloads/" + file, encoding='utf-8') as file_csv:
        headers, *rows = csv.reader(file_csv, delimiter=',')
        data_dict = Counter({row[0]: sum(map(int, row[1:])) for row in rows})
    with open("C:/Users/kandz/Downloads/" + prices, encoding='utf-8') as file_json:
        data_json = json.load(file_json)
        total = sum([data_dict[k] * data_json[k] for k in data_json])
    return total


lst = ['quarter1.csv', 'quarter2.csv', 'quarter3.csv', 'quarter4.csv']
print(sum([total_profit(file, 'prices.json') for file in lst]))
