"""
Секретное слово
Напишите программу для расшифровки секретного слова методом частотного анализа.

Формат входных данных
В первой строке задано зашифрованное слово. Во второй строке задано одно целое число
�
n – количество букв в словаре. В следующих
�
n строках записано, сколько раз конкретная буква алфавита встречается в этом слове – <буква>: <частота>.

Формат выходных данных
Программа должна вывести дешифрованное слово.

Примечание. Гарантируется, что частоты букв не повторяются.

Тестовые данные 🟢
Sample Input 1:

*!*!*?
3
а: 3
н: 2
с: 1
Sample Output 1:

ананас
Sample Input 2:

pop
2
д: 2
е: 1
Sample Output 2:

дед
"""
word_d = {}
word = input()
for l in word:
    word_d[l] = word_d.get(l, 0) + 1
abc = {k: int(v) for _ in range(int(input())) for k, v in [input().split(': ')]}
# print(word_d, abc, sep='\n')
for k, v in word_d.items():
    for key, value in abc.items():
        if v == value:
            word_d[k] = key
[print(word_d[i], end='') for i in word]
"""
___________________________________________________________________________________
"""
dct, word = {}, {}
s = input()
for c in s:
    word[c] = word.get(c, 0) + 1
for _ in range(int(input())):
    a, b = input().split(': ')
    dct[int(b)] = a
for c in s:
    print(dct[word[c]], end='')
