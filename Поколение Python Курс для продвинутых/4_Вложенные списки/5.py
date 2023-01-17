"""
Разбиение на чанки 🌶️
На вход программе подаются две строки, на одной символы, на другой число n. Из первой строки формируется список.

Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает
список из чанков указанной длины.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число n на отдельной
строке.

Формат выходных данных
Программа должна вывести указанный вложенный список.

Примечание. Не забудьте вызвать функцию chunked(), чтобы вывести результат 😀.

Тестовые данные 🟢
Sample Input 1:

a b c d e f
2
Sample Output 1:

[['a', 'b'], ['c', 'd'], ['e', 'f']]
Sample Input 2:

a b c d e f
3
Sample Output 2:

[['a', 'b', 'c'], ['d', 'e', 'f']]
Sample Input 3:

a b c d e f
6
Sample Output 3:

[['a', 'b', 'c', 'd', 'e', 'f']]
Sample Input 4:

a b c d e f r g b
2
Sample Output 4:

[['a', 'b'], ['c', 'd'], ['e', 'f'], ['r', 'g'], ['b']]
Sample Input 5:

a b
3
Sample Output 5:

[['a', 'b']]
"""


def chunked(s, n):
    elem = []
    res = []
    i = 0
    if len(s) <= n:
        res.append(s)
        return res
    for char in s:
        elem.append(char)
        if len(elem) == n:
            res.append(elem)
            elem = []
    if elem:
        res.append(elem)
    return res


s = input().split()
n = int(input())
print(chunked(s, n))

"""
__________________________________________________________________________________________________________________
"""


def chunked(symbols, n):
    result = []
    for i in range(0, len(symbols), n):
        result.append(symbols[i:i + n])
    return result