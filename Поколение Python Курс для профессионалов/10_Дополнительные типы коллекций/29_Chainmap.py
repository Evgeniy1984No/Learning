"""
Зоопарк
Вам доступен файл zoo.json, содержащий список JSON-объектов с данными об обитателях некоторого зоопарка. Ключом в каждом
объекте является название животного, значением — их количество в зоопарке:

[
   {
      "Axolotl": 11,
      "Poison Frog": 12,
      "Sonoran Toad": 6,
      "Tiger Salamander": 16
   },
   {
      "African Fish Eagle": 6,
      "Andean Condor": 8,
      "Black Vulture": 8,
      "Bufflehead Duck": 9,
      "Flamingo": 8,
      "Great Horned Owl": 16,
      "Hornbill": 1
   },
   ...
]
Напишите программу, которая определяет, сколько всего животных обитает в зоопарке, и выводит полученный результат.

Примечание 1. Гарантируется, что все ключи в JSON-объектах, различны.

Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 3. При открытии файла используйте явное указание кодировки UTF-8.
"""
import json
from collections import ChainMap

with open('C:/Users/kandz/Downloads/zoo.json', encoding='utf-8') as f1:
    data = ChainMap(*json.load(f1))
    count = sum(data.values())
    print(count)