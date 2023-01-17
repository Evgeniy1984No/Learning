"""
Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.

Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции строка s перейдет в строку "baba", после
выполнения двух и операций – в строку "bbaa", и дальнейшие операции не будут изменять строку s.

Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a. Если
операций потребуется более 1000, выведите Impossible.

Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки a,
или Impossible, если операций потребуется более 1000.

Условие задачи было изменено 12.09.2018
Sample Input 1:

ababa
a
b
Sample Output 1:

1
Sample Input 2:

ababa
b
a
Sample Output 2:

1
Sample Input 3:

ababa
c
c
Sample Output 3:

0
Sample Input 4:

ababac
c
c
Sample Output 4:

Impossible
"""


def count_replace(string, chars, chars_change):
    count = 0
    while chars in string:
        string = string.replace(chars, chars_change)
        count += 1
        if count > 1000:
            return "Impossible"
    return count


s, a, b = (input() for _ in range(3))
print(count_replace(s, a, b))

"""
________________________________________________________________________________________________
Below Uses generator
"""

# s, a, b = (input() for _ in range(3))
#
#
# def repl_gen(s, a, b):
#     while a in s:
#         s = s.replace(a, b)
#         yield True
#
#
# print('Impossible' if a in b and a in s else sum(repl_gen(s, a, b)))
