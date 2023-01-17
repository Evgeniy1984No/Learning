"""
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
Попробуем написать подобную систему.
На вход программе первой строкой передаётся количество dd известных нам слов, после чего на dd строках указываются эти 
слова. Затем передаётся количество ll строк текста для проверки, после чего ll строк текста.
Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:

4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic
Sample Output:

stepic
champignons
the
"""
abc_right = {}
mistakes = {}
for i in range(int(input())):
    word = input().lower()
    abc_right[word] = ''

for i in range(int(input())):
    line = [j for j in input().lower().split(' ')]
    for word in line:
        if word not in abc_right:
            mistakes[word] = ''

for key in mistakes.keys():
    print(key)


'''
______________________________________________________________________________________________________
dic = {input().lower() for i in range(int(input()))}

wrd = set()
for w in range(int(input())):
    wrd |= {i.lower() for i in input().split()}

print(*wrd.difference(dic), sep="\n")
'''