"""
В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: они говорили каким-то 
странным набором звуков.
В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр, 
т.е. заменяли каждый символ исходного сообщения на соответствующий ему другой символ. Биологи раздобыли ключ к шифру 
и теперь нуждаются в помощи:

Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. 
Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита, н
а второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, 
и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки, 
которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

Sample Input 1:

abcd
*d%#
abacabadaba
#*%*d*%
Sample Output 1:

*d*%*d*#*d*
dacabac
Sample Input 2:

dcba
badc
dcba
badc
Sample Output 2:

badc
dcba
"""


def coder(abc, arr):
    arr_code = []
    for i in arr:
        if i in abc:
            arr_code.append(abc[i])
    return arr_code


def decoder(abc, arr_code):
    arr = []
    for i in arr_code:
        for key, values in abc.items():
            if i == values:
                arr.append(key)
    return arr


abc_code = {}
abc = [i for i in input()]
code = [i for i in input()]
for i in range(len(abc)):
    abc_code[abc[i]] = code[i]
arr_code = [i for i in input()]
arr_decode = [i for i in input()]

print(*coder(abc_code, arr_code), sep='')
print(*decoder(abc_code, arr_decode), sep='')
'''
____________________________________________________________________________________________________
a,b,c,d=input(),input(),input(),input()
print(''.join(b[a.index(i)] for i in c))
print(''.join(a[b.index(i)] for i in d))
'''
