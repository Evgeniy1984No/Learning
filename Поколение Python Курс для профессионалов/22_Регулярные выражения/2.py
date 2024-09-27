"""
Популярность
В онлайн-школе BEEGEEK мы всегда следим за тем, насколько растет наша популярность. Для этого мы собираем публикации из
различных соцсетей, которые содержат вхождения строки beegeek в нижнем регистре. Мы оцениваем публикацию:

в
3
3 балла, если она начинается и заканчивается строкой beegeek
в
2
2 балла, если она только начинается или только заканчивается строкой beegeek
в
1
1 балл, если она содержит строку beegeek только внутри
в
0
0 баллов, если она не содержит строку beegeek
Напишите программу, которая определяет популярность онлайн-школы BEEGEEK путем суммирования баллов всех публикаций.

Формат входных данных
На вход программе подается произвольное число строк, каждая из которых представляет очередную публикацию.

Формат выходных данных
Программа должна определить, во сколько баллов оценивается каждая введенная публикация, и вывести сумму всех полученных
баллов.

Примечание 1. Если публикация представляет собой просто строку beegeek, то она оценивается в
2
2 балла.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

hi, beegeek
beegeek is an awesome place for programmers
beegeek rocks, rocks beegeek
i think beegeek is a great place to hangout
Sample Output 1:

8
Sample Input 2:

good morning everyone
i am going to school
and it is raining
Sample Output 2:

0
"""
from re import search
import sys


data = [line.strip() for line in sys.stdin]
three = [3 for i in data if search(r'^(beegeek).*\1$', i)]
two = [2 for i in data if search(r'^(beegeek)', i) or search(r'(beegeek)?', i)]
one = [1 for i in data if search(r'beegeek', i)]
print(sum(three) + sum(two) + sum(one))
