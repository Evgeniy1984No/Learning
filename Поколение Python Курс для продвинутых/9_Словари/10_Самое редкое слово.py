"""
На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего,
без учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести слово (в нижнем регистре), встречаемое реже всего.

Примечание 1. Программа не должна быть чувствительной к регистру, слова apple и Apple должна воспринимать как одинаковые.

Примечание 2. Слово — последовательность букв. Кроме слов в тексте могут присутствовать пробелы и знаки препинания
.,!?:;-, которые нужно игнорировать. Других символов в тексте нет.

Тестовые данные 🟢
Sample Input 1:

home sweet home
Sample Output 1:

sweet
Sample Input 2:

home sweet home sweet.
Sample Output 2:

home
"""

d = {}
for word in input().split():
    word_rev = word.strip('.,!?:;-').lower()
    d[word_rev] = d.get(word_rev, 0) + 1
print(min(d, key=lambda x: (d[x], x)))

