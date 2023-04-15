"""
Словарь синонимов
Вам дан словарь, состоящий из пар слов-синонимов. Повторяющихся слов в словаре нет. Напишите программу, которая для одного данного слова определяет его синоним.

Формат входных данных
На вход программе подается количество пар синонимов
�
n. Далее следует
�
n строк, каждая строка содержит два слова-синонима. После этого следует одно слово, синоним которого надо найти.

Формат выходных данных
Программа должна вывести одно слово, синоним введенного.

Примечание 1. Гарантируется, что синоним введенного слова существует в словаре.

Примечание 2. Все слова в словаре начинаются с заглавной буквы.

Тестовые данные 🟢
Sample Input 1:

4
Awful Terrible
Beautiful Pretty
Great Excellent
Generous Bountiful
Pretty
Sample Output 1:

Beautiful
Sample Input 2:

3
Kind Affable
Intellect Mind
Popular Celebrated
Popular
Sample Output 2:

Celebrated
"""
# d = {}
# for _ in range(int(input())):
#     key, value = input().split()
#     d.update({key: value})
d = {k: v for _ in range(int(input())) for k, v in [input().split()]}
word = input()
for k, v in d.items():
    if k == word:
        print(v)
    elif v == word:
        print(k)

"""
_______________________________________________________________________
"""
words = {}
for _ in range(int(input())):
    a, b = input().split()
    words[a], words[b] = b, a
print(words[input()])
