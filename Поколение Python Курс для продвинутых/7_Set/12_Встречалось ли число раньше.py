"""
Встречалось ли число раньше?
На вход программе подается строка текста, содержащая числа. Для каждого числа выведите слово YES (в отдельной строке),
если это число ранее встречалось в последовательности или NO, если не встречалось.

Формат входных данных
На вход программе подается строка текста, содержащая числа, разделенные символом пробела.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Ведущие нули в числах должны игнорироваться.

Тестовые данные 🟢
Sample Input 1:

1 1 2 2 5 5 5 5 6 7 8
Sample Output 1:

NO
YES
NO
YES
NO
YES
YES
YES
NO
NO
NO
Sample Input 2:

10 5 48 6 38 1
Sample Output 2:

NO
NO
NO
NO
NO
NO
Sample Input 3:

1 1 1 1 1 1 1 1 1
Sample Output 3:

NO
YES
YES
YES
YES
YES
YES
YES
YES
Sample Input 4:

1 2 3 002 03 4 5 05
Sample Output 4:

NO
NO
NO
YES
YES
NO
NO
YES
"""
s = [int(i) for i in input().split()]
s_check = set()
for i in s:
    if i in s_check:
        print('YES')
    else:
        s_check.add(i)
        print('NO')

"""
__________________________________________________________________________________________
"""

s = set()
for item in input().split():
    print(["NO", "YES"][item in s])
    s.add(item)
