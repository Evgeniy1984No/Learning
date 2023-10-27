"""
Вам доступен словарь data с четным количеством элементов. Дополните приведенный ниже код, чтобы он вывел данный словарь,
 расположив его элементы по следующему правилу: первый, последний, второй, предпоследний, третий, и так далее.

Примечание. Например, если бы словарь data имел вид:

data = OrderedDict(key1='value1', key2='value2', key3='value3', key4='value4')
то программа должны была бы вывести:

OrderedDict([('key1', 'value1'), ('key4', 'value4'), ('key2', 'value2'), ('key3', 'value3')])
"""
from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                    'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
d = []
[d.append(data.popitem(last=rule)) for rule in [False, True] * (len(data)//2)]
print(OrderedDict(d))
# *****************************************************************************************************************
data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                    'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
data = OrderedDict([data.popitem(last=i % 2) for i in range(len(data))])
print(data)
