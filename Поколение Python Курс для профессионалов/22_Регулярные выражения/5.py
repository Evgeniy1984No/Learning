"""
HTML 🌶️🌶️
HTML-элементы — основа языка HTML. Каждый HTML-элемент обозначается начальным (открывающим) и конечным (закрывающим)
тегами. Открывающий и закрывающий теги содержат имя элемента. Открывающий тег может содержать дополнительную информацию
— атрибуты и значения атрибутов:

<b>BeeGeek</b>
<a href="https://stepik.org">Stepik</a>
В примере выше тег <b> не содержит никаких атрибутов, а тег <a> содержит атрибут href со значением https://stepik.org.

Напишите программу, которая находит во фрагменте HTML-страницы все атрибуты каждого тега.

Формат входных данных
На вход программе подается произвольное количество строк, которые образуют фрагмент HTML-страницы.

Формат выходных данных
Программа должна найти в введенном фрагменте HTML-страницы все теги и вывести их, указав для каждого соответствующие
атрибуты. Теги вместе со всеми атрибутами должны быть расположены каждый на отдельной строке, в следующем формате:

<тег>: <атрибут>, <атрибут>, ...
Теги, а также атрибуты тегов, должны быть расположены в лексикографическом порядке.

Примечание 1. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Примечание 2. Некоторые теги не требуют закрытия. Об этом можно почитать здесь.

Sample Input 1:

<p><a href="https://stepik.org">Stepik</a></p>
<div class="catalog"><a href="https://stepik.org/catalog">Study hard. Teach harder</a></div>
Sample Output 1:

a: href
div: class
p:
Sample Input 2:

<div id="oldie-warning" class="do-not-print">
    <p>
        <strong>Notice:</strong> Your browser is <em>ancient</em>. Please
        <a href="http://browsehappy.com/">upgrade to a different browser</a> to experience a better web.
    </p>
</div>
Sample Output 2:

a: href
div: class, id
em:
p:
strong:
"""
import re
import sys

data = [line.strip() for line in sys.stdin]
tags = []
res = {}
for line in data:
    tags.extend(re.findall(r'<(\w.*?)>', line))
for i in sorted(tags):
    m = re.search(r'(\w+) ', i)
    att = re.search(r'\b(\w+)\b=', i)   #\b(\w+)\b= - для атрибутов
    if att:
        res[m.group(1)] = res.get(m.group(1), []) + sorted(re.findall(r'([\w-]+)=', i))
        # print(re.findall(r'([A-Za-z-]+)=', i))
    else:
        res[i] = []
[print(f'{k}: {', '.join(sorted(set(v)))}') for k, v in res.items()]


# *****************************************************************************************************************

res = {}
for line in sys.stdin:
    for tag, params in re.findall(r'<(\w+)(.*?)>', line.strip()):
        res.setdefault(tag, set()).update(re.findall(r'([\w-]+)=', params))

for key in sorted(res):
    print(f'{key}: {", ".join(sorted(res[key]))}')