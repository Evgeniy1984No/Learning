"""
В поисках слов 😋
Дана последовательность слов. Напишите программу, которая выводит наименее часто встречаемое слово в этой
последовательности. Если таких слов несколько, программа должна вывести их все.

Формат входных данных
На вход программе подается последовательность слов, разделенных пробелом.

Формат выходных данных
Программа должна определить наименее часто встречаемое слово в введенной последовательности и вывести его в нижнем
регистре. Если таких слов несколько, программа должна вывести их все в лексикографическом порядке, в нижнем регистре,
разделяя запятой и пробелом.

Примечание 1. Программа должна игнорировать регистр. То есть, например, слова Python и python считаются одинаковыми.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

Арбуз Малина Малина Арбуз Клубника арбуз банан малина вишня черешня вишня арбуЗ
Sample Output 1:

банан, клубника, черешня
Sample Input 2:

арбуз МалинА клубника Банан Вишня Черешня
Sample Output 2:

арбуз, банан, вишня, клубника, малина, черешня
Sample Input 3:

арбуз черешня малина малина арбуз арбуз Банан малина вишня черешня вишня арбуз
Sample Output 3:

банан
"""
from collections import Counter

data = Counter(map(str.lower, input().split()))
low = data.most_common()[-1][1]
print(', '.join([i[0] for i in sorted(data.most_common()) if i[1] == low]))

