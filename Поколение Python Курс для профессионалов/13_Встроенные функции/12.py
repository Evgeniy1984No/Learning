"""
Математические выражения
Напишите программу, которая принимает на вход произвольное количество строк, содержащих корректные математические
выражения, и выводит значение наибольшего из них.

Формат входных данных
На вход программе подается произвольное количество строк, каждое из которых содержит корректное математическое
выражение.

Формат выходных данных
Программа должна вычислить значения введенных выражений и вывести наибольшее.

Примечание 1. Под корректным математическим выражением подразумевается выражение, полностью соответствующее синтаксису
языка Python.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

1 + 2 + 3
2 * 8
10 * 10 - 1
Sample Output 1:

99
Sample Input 2:

1 + 1 + 1 + 1 + 1
2 * 2 * 2 * 2 * 2
3 // 3 // 3 // 3 // 3
4 - 4 - 4 - 4 -4
Sample Output 2:

32
Sample Input 3:

(2**3 + 2) * 10 - 4
100
((97 - 19)**4) * 0
1 + 2 - 3 * 4 // 5
Sample Output 3:

100
"""
import sys

arr = [eval(i) for i in sys.stdin]
print(max(arr))
