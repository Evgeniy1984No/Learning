"""
Книги на прочтение 🌶️
Ученики
10
10 класса онлайн-школы BEEGEEK получили задание прочесть на летних каникулах три книги:

"Что такое математика?";
"Математическая составляющая";
"100 гениальных идей по математике".
Оказалось, что
�
n учеников прочитали первую книгу,
�
m учеников — вторую,
�
k учеников — третью. Также известно, что
�
x учеников прочли первую или вторую, или обе эти книги,
�
y учеников — вторую или третью, или обе,
�
z учеников — первую и третью, или хотя бы одну из этих двух книг. Полностью выполнили задание только
�
t учеников. Всего в
10
10 классе учится
�
a учеников. Напишите программу, которая выводит сколько учеников:

прочитали только одну книгу;
прочитали две книги;
не прочитали ни одной из рекомендованных книг.
Формат входных данных
На вход программе подаются числа
�
,
�
,
�
,
�
,
�
,
�
,
�
,
�
n,m,k,x,y,z,t,a, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести три числа в соответствии с условием задачи, каждое на отдельной строке.

Тестовые данные 🟢
Sample Input:

19
18
22
32
33
35
2
50
Sample Output:

29
12
7
"""
n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]
one = n-(m+n-x-t)-(n+k-z-t)-t + m-(m+n-x-t)-(m+k-y-t)-t + k-(n+k-z-t)-(m+k-y-t)-t
two = m+n-x-t + n+k-z-t + m+k-y-t
print(one)
print(two)
print(a-one-two-t)
