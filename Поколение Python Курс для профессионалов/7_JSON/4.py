"""
Элементы JSON
Напишите программу, которая принимает на вход описание одного объекта в формате JSON и выводит все пары ключ-значение
этого объекта.

Формат входных данных
На вход программе подается корректное описание одного объекта в формате JSON.

Формат выходных данных
Программа должна вывести все пары ключ-значение введенного объекта, разделяя ключ и значение двоеточием, каждую на
отдельной строке. Если значением ключа является список, то все его элементы должны быть выведены через запятую.

Примечание 1. Пары ключ-значение при выводе должны располагаться в своем исходном порядке.

Примечание 2. Для считывания произвольного числа строк используйте потоковый ввод sys.stdin.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

{"size": 36, "style": "bold", "name": "text1", "alignment": "center"}
Sample Output 1:

size: 36
style: bold
name: text1
alignment: center
Sample Input 2:

{
 "type": "donut",
 "name": "Cake",
 "tastes": ["chocolate", "cream", "strawberry"]
}
Sample Output 2:

type: donut
name: Cake
tastes: chocolate, cream, strawberry
"""
import json
import sys

json_input = json.loads(sys.stdin.read())
for k, v in json_input.items():
    if type(v) != list:
        print(f'{k}: {v}')
    else:
        print(f'{k}: ', end='')
        print(*v)
# *********************************************************************************************************************
[[print(f'{k}: {", ".join(map(str, v))}')] if isinstance(v, list) else print(f'{k}: {v}') for k, v in json_input.items()]

