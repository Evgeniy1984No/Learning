"""
Разные типы
Вам доступен файл data.json, содержащий список различных объектов:

[
   "nwkWXma",
   null,
   {
      "ISgHT": "dIUbf"
   },
   "Pzt",
   "BXcbGVTE",
   ...
]
Напишите программу, которая создает список, элементами которого являются объекты из списка, содержащегося в файле
data.json, измененные по следующим правилам:

если объект является строкой, в его конец добавляется восклицательный знак
если объект является числом, он увеличивается на единицу
если объект является логическим значением, он инвертируется
если объект является списком, он удваивается
если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null
если объект является пустым значением (null), он не добавляется
Полученный список программа должна записать в файл updated_data.json.

Примечание 1. Например, если бы файл data.json имел вид:

["Hello", 179, true, null, [1, 2, 3], {"key": "value"}]
то программа должна была бы создать файл updated_data.json со следующим содержанием:

["Hello!", 180, false, [1, 2, 3, 1, 2, 3], {"key": "value", "newkey": null}]
Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 3. При открытии файла используйте явное указание кодировки UTF-8.
"""
import json


def my_map(elem):
    if type(elem) == str:
        return elem + '!'
    if type(elem) == int:
        return elem + 1
    if type(elem) == bool:
        return not elem
    if type(elem) == list:
        return elem * 2
    if type(elem) == dict:
        elem.update({"newkey": None})
        return elem


with open('C:/Users/kandz/Downloads/data.json', encoding='utf-8') as file_input:
    lst_json = list(filter(lambda x: x is not None, json.load(file_input)))

with open('updated_data.json', 'w', encoding='utf-8') as file_output:
    json.dump(list(map(my_map, lst_json)), file_output)

# **********************************************************************************************************************
opers = {'str': lambda x: x + '!',
         'int': lambda x: x + 1,
         'float': lambda x: x + 1,
         'bool': lambda x: not x,
         'list': lambda x: x * 2,
         'dict': lambda x: x | {'newkey': None}}

with (open('C:/Users/kandz/Downloads/data.json', encoding='utf8') as fi,
      open('updated_data.json', 'w', encoding='utf8') as fo):
    json.dump([opers[type(i).__name__](i) for i in json.load(fi) if type(i).__name__ in opers], fo, indent=3)
