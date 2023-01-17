"""
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле
name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Эквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass

Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от
одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.

Sample Input:

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
Sample Output:

A : 3
B : 1
C : 2
"""

import json

data = json.loads(input())
parents = {}
classes = {c['name']: c['parents'] for c in data}


def is_parent(p_parent, child):
    if p_parent in classes[child]:
        return True
    else:
        for parent in classes[child]:
            if is_parent(p_parent, parent):
                return True


for name in classes:
    if name not in parents:
        parents[name] = 1
    for key in classes.keys():
        if is_parent(name, key):
            parents[name] += 1

for name in sorted(parents):
    print(name, ':', parents[name])
"""
______________________________________________________________________________________
"""


def test(parent, child):
    for index in data:
        if parent in index['parents']:
            child.add(index['name'])
            child = test(index['name'], child)
    return child


data = json.loads(input())
data.sort(key=(lambda x: x['name']))
for i in data:
    print(i['name'], ':', len(test(i['name'], child=set())) + 1)
