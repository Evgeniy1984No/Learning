"""
Восстановление недостающих ключей
Вам доступен файл people.json, содержащий список JSON-объектов. Причем у различных объектов может быть различное количество ключей:

[
   {
      "age": 33,
      "country": "Lesotho",
      "phone": "(927) 316-2249",
      "family_status": "married",
      "email": "neonatus@outlook.com"
   },
   {
      "age": 25,
      "country": "Guinea",
      "name": "Dorey",
      "children": "yes",
      "email": "ismail@gmail.com",
      "university": "Khalifa University",
      "family_status": "married"
   },
   ...
]
Напишите программу, которая добавляет в каждый JSON-объект из данного списка все недостающие ключи, присваивая этим
ключам значение null. Ключ считается недостающим, если он присутствует в каком-либо другом объекте, но отсутствует в
данном. Программа должна создать список с обновленными JSON-объектами и записать его в файл updated_people.json.

Примечание 1. JSON-объекты в создаваемом программой списке должны располагаться в своем исходном порядке. Порядок ключей
в JSON-объектах не важен.

Примечание 2. Например, если бы файл people.json имел вид:

[
   {
      "age": 33,
      "country": "Lesotho"
   },
   {
      "age": 25,
      "country": "Guinea",
      "name": "Dorey"
   }
]
то программа должна была создать файла updated_people.json со следующим содержанием:

[
   {
      "age": 33,
      "country": "Lesotho"
      "name": null
   },
   {
      "age": 25,
      "country": "Guinea",
      "name": "Dorey"
   }
]
Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
"""
import json

with open('C:/Users/kandz/Downloads/people.json', encoding='utf-8') as f1:
    data = json.load(f1)
    print(data)
    d_keys = set()
    for d in data:
        d_keys |= set(d.keys())
    [d.setdefault(k) for k in d_keys for d in data]
with open('C:/Users/kandz/Downloads/updated_people.json', 'w', encoding='utf-8') as f2:
    json.dump(data, f2)
