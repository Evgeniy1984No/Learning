"""
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
abababa
abababa
abababa

Sample Input 1:

abababa
aba
Sample Output 1:

3
Sample Input 2:

abababa
abc
Sample Output 2:

0
Sample Input 3:

abc
abc
Sample Output 3:

1
Sample Input 4:

aaaaa
a
Sample Output 4:

5
"""


def count_in_string(string_1, string_2):
    i = 0
    count = 0
    while string_2 in string_1[i:]:
        if string_1[i:].startswith(string_2):
            count += 1
        i += 1
    return count


string_1, string_2 = (input() for _ in range(2))
print(count_in_string(string_1, string_2))
"""
_________________________________________________________________________________________
"""
s = input()
t = input()
ans = 0
for i in range(len(s)):
    if s[i:].startswith(t):
        ans += 1

print(ans)
"""
_______________________________________________________________________________________________________________
Optimization solution
"""
s, t = [input() for i in range(2)]
count, i = 0, 0
while s.find(t, i) >= 0:
    pos = s.find(t, i)
    count += 1
    i = pos + 1

print(count)
