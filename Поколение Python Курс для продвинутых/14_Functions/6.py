"""
Хороший пароль
Хороший пароль по условиям этой задачи состоит как минимум из
7
7 символов, содержит хотя бы одну цифру, заглавную и строчную букву. Напишите программу со встроенной функцией any() для
определения хорош ли введенный пароль.

Формат входных данных
На вход программе подаётся одна строка текста.

Формат выходных данных
Программа должна вывести YES, если строка – хороший пароль, и NO в противном случае.

Тестовые данные 🟢
Sample Input 1:

abcABC9
Sample Output 1:

YES
Sample Input 2:

abAB34
Sample Output 2:

NO
Sample Input 3:

DFSDFSDFSDsdfjsdfnsm
Sample Output 3:

NO
"""
pwd = input()
print(['NO', 'YES'][all([len(pwd) >= 7, any(map(lambda s: s.isdigit(), pwd)), any(map(lambda s: s.islower(), pwd)), any(map(lambda s: s.isupper(), pwd))])])