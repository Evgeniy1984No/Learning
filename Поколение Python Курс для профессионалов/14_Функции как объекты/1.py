"""
Новый print()
Напишите программу, которая переопределяет встроенную функцию print() так, чтобы она печатала все переданные строковые
аргументы в верхнем регистре.

Примечание 1. Значения sep и end также должны переводиться в верхний регистр.

Примечание 2. В тестирующую систему сдайте программу, содержащую только переопределенную функцию print(), но не код,
вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
   Задача представлена исключительно в учебных целях, на практике применять подобное, конечно, не следует.

Sample Input 1:

print('beegeek', [1, 2, 3], 4)
Sample Output 1:

BEEGEEK [1, 2, 3] 4
Sample Input 2:

print('bee', 'geek', sep=' and ', end=' wow')
Sample Output 2:

BEE AND GEEK WOW
Sample Input 3:

words = ('black', 'white', 'grey', 'black-1', 'white-1', 'python')
print(*words, sep=' to ', end=' LOVE')
Sample Output 3:

BLACK TO WHITE TO GREY TO BLACK-1 TO WHITE-1 TO PYTHON LOVE
"""
old_print = print


def print(*args, **kwargs):
    kwargs = dict(zip(kwargs.keys(), map(str.upper, kwargs.values())))
    args = map(lambda x: x.upper() if isinstance(x, str) else x, args)
    old_print(*args, **kwargs)


# *******************************************************************************************************************
def print(*args, sep=' ', end='\n'):
    args = (i.upper() if isinstance(i, str) else i for i in args)
    old_print(*args, sep=sep.upper(), end=end.upper())


print('beegeek', [1, 2, 3], 4)
print('bee', 'geek', sep=' and ', end=' wow')