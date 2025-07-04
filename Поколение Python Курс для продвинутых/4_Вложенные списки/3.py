"""
Треугольник Паскаля 2
На вход программе подается натуральное число nn. Напишите программу, которая выводит первые nn строк треугольника Паскаля.

Формат входных данных
На вход программе подается число n \, (n \ge 1)n (n≥1).

Формат выходных данных
Программа должна вывести первые nn строк треугольника Паскаля, каждую на отдельной строке в соответствии с образцом.

Тестовые данные 🟢
Sample Input 1:

4
Sample Output 1:

1
1 1
1 2 1
1 3 3 1
Sample Input 2:

5
Sample Output 2:

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
Sample Input 3:

2
Sample Output 3:

1
1 1
"""
n = int(input())

li = [1]
print(*li)
for i in range(n-1):
    for j in range(len(li) - 1):
        li[j] = li[j] + li[j + 1]

    li.insert(0, 1)
    print(*li)
