"""
Даны по
10
10-балльной шкале оценки по физике трех учеников. Напишите программу, которая выводит множество оценок третьего ученика,
которые не встречаются ни у первого, ни у второго ученика.

Формат входных данных
На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого ученика на отдельной
строке).

Формат выходных данных
Программа должна вывести множество оценок в порядке убывания на одной строке, разделенных пробелами, в соответствии с
условием задачи.

Примечание. Оценка ученика находится в диапазоне от
0
0 до
10
10 включительно.

Тестовые данные 🟢
Sample Input 1:

1 5 4 2 5 6 6 2 3 3 5 2
2 3 5 1 2 1 2 6 7 1 1 6
1 4 6 9 8 7 0 9 0 9 8 10
Sample Output 1:

10 9 8 0
Sample Input 2:

2 9 2 4 6 10
2 2 4 5 2 10
2 3 4 5 3 9
Sample Output 2:

3
Sample Input 3:

3 4 5 6 2 10 3 9 8 8 4
5 7 8 9 2 7 4 6 8 2 5
2 6 7 1 3 6 5 9 2 6 10
Sample Output 3:

1
"""
s1, s2, s3 = [set(int(i) for i in input().split()) for _ in range(3)]
res = s3.difference(s1.union(s2))
print(*sorted(res, reverse=True))