"""
Анаграммы 1
Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово
(или словосочетание). Например, английские слова evil и live – это анаграммы.

На вход программе подаются два слова. Напишите программу, которая определяет, являются ли они анаграммами.

Формат входных данных
На вход программе подаются два слова, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести YES если слова являются анаграммами и NO в противном случае.

Тестовые данные 🟢
Sample Input 1:

thing
night
Sample Output 1:

YES
Sample Input 2:

cat
rat
Sample Output 2:

NO
Sample Input 3:

tea
eat
Sample Output 3:

YES
"""
d = {}
flag = 1
for l in input():
    d[l] = d.get(l, 0) + 1
for w in input():
    if w not in d:
        flag = 0
        break
    d[w] = d[w] - 1
for value in d.values():
    if value != 0:
        flag = 0
print(('NO', 'YES')[flag])

"""
______________________________________________________________________________
"""
d = {}
for c in input().lower():
    d[c] = d.get(c, 0) + 1
for c in input().lower():
    d[c] = d.get(c, 0) - 1

print(('NO', 'YES')[set(d.values()) == {0}])
