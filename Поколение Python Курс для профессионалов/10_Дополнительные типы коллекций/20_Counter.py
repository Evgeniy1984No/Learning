"""
 поисках слов 🥳
Дана последовательность слов. Напишите программу, которая выводит наиболее часто встречаемое слово в этой
последовательности. Если таких слов несколько, программа должна вывести то, которое больше в лексикографическом
сравнении.

Формат входных данных
На вход программе подается последовательность слов, разделенных пробелом.

Формат выходных данных
Программа должна определить наиболее часто встречаемое слово в введенной строке и вывести его в нижнем регистре. Если
таких слов несколько, программа должна вывести то, которое больше в лексикографическом сравнении, также в нижнем
регистре.

Примечание 1. Программа должна игнорировать регистр. То есть, например, слова Python и python считаются одинаковыми.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

Арбуз Малина арбуЗ Клубника арбуз банан малина черешня вишня арбуз клубника Банан
Sample Output 1:

арбуз
Sample Input 2:

МаЛиНа клубника Арбуз банаН Малина Черешня вишня арбуз клубника банан
Sample Output 2:

малина
Sample Input 3:

малина малина клубника арбуз банан малина черешня вишня арбуз клубника банан малина
Sample Output 3:

малина
"""
from collections import Counter

data = Counter(map(str.lower, input().split()))
print(max(list(data.items()), key=lambda x: (x[1], x[0]))[0])
# *********************************************************************************************************************
print(max(data, key=lambda x: (data[x], x)))