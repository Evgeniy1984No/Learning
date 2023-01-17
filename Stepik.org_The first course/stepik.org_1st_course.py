# name = 'Arya'
# x = int(input())
# h = int(input())
# m = int(input())
# print((h + x // 60) + (m + x % 60) // 60, m + x % 60, sep='\n')
# print((h * 60 + m + x) // 60, (h * 60 + m + x) % 60, sep='\n')

# x = 5
# y = 10
# print(y > x * x or y >= 2 * x and x < y)
#
# a = True
# b = False
# print(a and b or not a and not b)
'''
year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Високосный')
else:
    print('Обычный')
'''

# a = int(input())
# b = int(input())
# c = int(input())
#
# p = (a + b + c) / 2
# S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#
# print(S)

# a = float(input())
# b = float(input())
# operator = str(input())

# if operator == '+':
#     print(a + b)
# elif operator == '-':
#     print(a - b)
# elif operator == '/':
#     if b == 0:
#         print('Деление на 0!')
#     else:
#         print(a / b)
# elif operator == '*':
#     print(a * b)
# elif operator == 'mod':
#     if b == 0:
#         print('Деление на 0!')
#     else:
#         print(a % b)
# elif operator == 'pow':
#     print(a ** b)
# elif operator == 'div':
#     if b == 0:
#         print('Деление на 0!')
#     else:
#         print(a // b)
# type_of_room = input()
#
# if type_of_room == 'треугольник':
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     p = (a + b + c) / 2
#     S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# elif type_of_room == 'прямоугольник':
#     a = int(input())
#     b = int(input())
#     S = a * b
# elif type_of_room == 'круг':
#     r = int(input())
#     S = 3.14 * r ** 2
# print(S)
'''
a = int(input())
b = int(input())
c = int(input())

if a > c >= b or a >= c > b:
    a, b, c, = str(a), str(b), str(c)
    print('a' + a, 'b' + b,'c' + c, sep='\n')
elif a > b >= c or a >= b > c:
    a, b, c, = str(a), str(b), str(c)
    print('a' + a, 'c' + c, 'b' + b, sep='\n')
elif b > a >= c or b >= a > c:
    a, b, c, = str(a), str(b), str(c)
    print('b' + b, 'c' + c, 'a' + a, sep='\n')
elif b > c >= a or b >= c > a:
    a, b, c, = str(a), str(b), str(c)
    print('b' + b, 'a' + a, 'c' + c, sep='\n')
elif c > a >= b or c >= a > b:
    a, b, c, = str(a), str(b), str(c)
    print('c' + c, 'b' + b, 'a' + a, sep='\n')
elif c > b >= a or c >= b > a:
    a, b, c, = str(a), str(b), str(c)
    print('c' + c, 'a' + a, 'b' + b, sep='\n')
else:
    a, b, c, = str(a), str(b), str(c)
    print('a' + a, 'b' + b, 'c' + c, sep='\n')

Оптимальное решение:
a,b,c=int(input()),int(input()),int(input())
maxim=a
minim=b
if b>a:
    maxim=b
    minim=a
if c>maxim:
    maxim=c
if c<minim:
    minim=c
ost=a+b+c-minim-maxim
print(maxim)
print(minim)
print(ost)
'''

'''
n = int(input())
var_1 = 'программист'
var_2 = 'программиста'
var_3 = 'программистов'


if n <= 100:
    modul = n % 10
    if modul == 0 or 5 <= n <= 19 or 5 <= modul <= 9:
        print(n, var_3)
    elif modul == 1:
        print(n, var_1)
    else:
        print(n, var_2)
elif n <= 1000:
    modul = n % 100
    if modul <= 19:
        if modul == 0 or 5 <= modul <= 19:
            print(n, var_3)
        elif modul == 1:
            print(n, var_1)
        else:
            print(n, var_2)
    else:
        modul = modul % 10
        if modul == 0 or 5 <= modul <= 19:
            print(n, var_3)
        elif modul == 1:
            print(n, var_1)
        else:
            print(n, var_2)
print(modul)
Оптимальное решение:
i=int(input())
d=i%10
h=i%100
if d==1 and h!=11:
    s=""
elif 1<d<5 and not 11<h<15:
    s="а"
else:
    s="ов"
print(i," программист"+s)
'''

'''
number_of_ticket = int(input())
left = number_of_ticket // 10**3
right = number_of_ticket % 10**3

left_1 = left // 10**2
left_2 = left // 10 % 10
left_3 = left % 10

right_1 = right // 10**2
right_2 = right // 10 % 10
right_3 = right % 10

sum_left = left_1 + left_2 + left_3
sum_right = right_1 + right_2 + right_3
# print(left, left_1, left_2, left_3, '\n' + str(right), right_1, right_2, right_3)
if sum_right == sum_left:
    print('Счастливый')
else:
    print('Обычный')

a, b, c, d, e, f = input()
Оптимальное реешение:
a, b, c, d, e, f = input()
n= int(a)+int (b)+int(c)
m= int(d)+int (e)+int(f)
if n==m:
    print ('Счастливый')
else:
    print ('Обычный')
'''
# s = 0
# a = int(input())
#
# while a != 0:
#     s = s + a
#     a = int(input())
# print(s)
'''
a = int(input())
b = int(input())
i = 0
d = a * b
if a and b != 1:
    while i <= d:
        i += 1
        if i % a == 0 and i % b == 0:
            d = i
            print(d)
else:
    print(1)
Оптимальное решение:
a = int(input())
b = int(input())
d = a
while d % b:
    d += a
print(d)
'''

'''
i = 0
s = 1
while i < s:
    s = int(input())
    if 10 <= s <= 100:
        print(s)
    if s < 10:
        continue
    if s > 100:
        break
Оптимальное решение:
a = 0
while a <= 100:
    a = int(input())
    if 10 <= a <= 100:
        print(a)
'''

'''
print('Введите натуральных числа не больше 10')
a = int(input())
b = int(input())
c = int(input())
d = int(input())
while a > 10 or b > 10 or c > 10 or d > 10 or a <= 0 or b <= 0 or c <= 0 or d <= 0 or a > b or c > d:
    print('Введите натуральных числа не больше 10')
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
print(end='\t')
for first_string in range(c, d+1):
    print(first_string, end='\t')
print()
for i in range(a, b+1):
    print(i, end='\t')
    for j in range(c, d+1):
        print(i*j, end='\t')
    print()
'''

'''
# a, b = (int(i) for i in input().split())
a, b = int(input()), int(input())
s = 0
count = 0
for j in range(a, b+1):
    if j % 3 == 0:
        s += j
        count += 1
print(s / count)
'''

'''
GC = input()
g_value = GC.upper().count('g'.upper())
c_value = GC.upper().count('c'.upper())
print((g_value + c_value) / len(GC) * 100)
'''

'''
Условие задачи: 
Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ
и количество его повторений в этой позиции строки. Напишите программу, которая считывает строку, кодирует её 
предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать 
регистр символов.
s = input()
new_s = ''
count = 1
i = 0
while i <= len(s) - 1:
    char = s[i]
    i_next = i + 1

    while i_next < len(s):
        if char == s[i_next]:
            count += 1
            i_next += 1
            i += 1
        else:
            i = i_next - 1
            break
    new_s += char + str(count)
    count = 1
    i += 1
print(new_s)
Оптимальное решение:
genome = input()+' '
s = 0
n=genome[0]
for i in genome:       
    if n!=i:
        print(n + str(s), end = '')
        s=0
        n=i
    s+=1
'''

'''
Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого 
списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент, 
находящий на противоположном конце этого списка. 
Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
Если на вход пришло только одно число, надо вывести его же.
Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
Sample Input 1:
1 3 5 6 10
Sample Output 1:
13 6 9 15 7

a = [int(i) for i in input().split()]
index = 0
s = 0
b = []
if len(a) == 1:
    print(*a)
else:
    for index in range(len(a)):
        if index == len(a)-1:
            s = a[index-1] + a[0]
            b += [s]
        else:
            s = a[index-1] + a[index+1]
            b += [s]
    print(*b)
'''

'''
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, 
которые встречаются в нём более одного раза.
Для решения задачи может пригодиться метод sort списка.
Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.

Sample Input 1:
4 8 0 3 4 2 0 3
Sample Output 1:
0 3 4
Sample Input 2:
10
Sample Output 2:


a = [int(i) for i in input().split()]
a.sort()
index = 0
print(a, len(a))
b = []
index_b = 0
if len(a) == 1:
    del a[index]
elif a[len(a)-1] != a[len(a)-2] and len(a) != 2:
    del a[len(a)-1]

while index < len(a):
    print('index =', index, a, len(a))
    if index == len(a)-1:
        break
    elif a[index] == a[index+1]:
        del a[index+1]
        b.append(a[index])
        index = 0
    else:
        index += 1
while index_b < len(b):
    if index_b == len(b)-1:
        break
    elif b[index_b] == b[index_b+1]:
        del b[index_b+1]
        index_b = 0
    else:
        index_b += 1
print(*b)

Оптимальное решение:
a, b = [int(i) for i in input().split()], []
for i in a:
    if a.count(i) > 1 and b.count(i) == 0:
        b.append(i)
for i in b:
    print(i, end=" ")
'''
'''
Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор, пока сумма введённых чисел 
не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.
Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0, после этого 
считывание продолжать не нужно.
В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем, что сумма этих чисел равна нулю и выводим 
сумму их квадратов, не обращая внимания на то, что остались ещё не прочитанные значения.

a = [int(input())]
q = 0
s = a[0]

while s != 0:
    a.append(int(input()))
    s = a[0]
    for i in a:
        s += i
    if s == a[0]:
        s = 0
for j in a:
    q += j**2
print(q)

Оптимальное решение:
s, d = 0, 0
while True:
    a = int(input())
    s += a
    d += a*a
    if s == 0:
        break
print(d)
'''

'''
Напишите программу, которая выводит часть последовательности 
1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... 
(число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое число 
n — столько элементов последовательности должна отобразить программа. На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

a = []
b = []
i = 1
n = int(input())
while n < 0:
    n = int(input())

for j in range(n):
    a.append([i] * i)
    length_index = len(a[j])
    for add in range(length_index):
        b.append(a[j][add])
    i += 1
b = b[:n]
for k in b:
    print(k, end=' ')

Оптимальное решение:
n = int(input())
count = 0
curr = 1
for i in range(n):
    print(curr, end=' ')
    count += 1
    if count == curr:
        curr += 1
        count = 0
'''

'''
Напишите программу, которая считывает список чисел lstlst из первой строки и число xx из второй строки, которая выводит 
все позиции, на которых встречается число xx в переданном списке lstlst.
Позиции нумеруются с нуля, если число xx не встречается в списке, вывести строку "Отсутствует" 
(без кавычек, с большой буквы).
Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.

Sample Input 1:
5 8 2 7 8 8 2 4
8
Sample Output 1:
1 4 5

lst = [int(i) for i in input().split()]
x = int(input())
index = 0

if x not in lst:
    print('Отсутствует')
else:
    for j in lst:
        if j == x:
            print(index, end=' ')
        index += 1

l = [int(i) for i in input().split()]
x = int(input())
if not x in l: print('Отсутствует')
for i in range(len(l)):
    if l[i]==x: print(i, end = ' ')
    '''

'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк. После последней 
строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).
Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой 
матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.
В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

Sample Input 1:
9 5 3
0 7 -1
-5 2 9
end
Sample Output 1:
3 21 22
10 6 19
20 16 -1

Sample Input 2:
1
end
Sample Output 2:
4


a = []
row = []
new_row = []
b = []
while True:
    enter = input().split()
    for i in enter:
        if i != 'end':
            row.append(int(i))
        else:
            row.append(i)
    # print(row)
    a.append(row)
    row = []
    if a[-1] == ['end']:
        break
del a[len(a) - 1]
print(a)
j = 0

for i in range(len(a)):
    # строка = a[i]
    row = a[i]
    print('ROW a[i] =', row)
    while j < len(row):
        print('LEN(ROW)=', len(row))
        print(a[i][j])
        print('i=', i, 'j=', j)
        if i == 0 and j != len(row) - 1 and len(a) != 1:
            element = a[i - 1][j] + a[i + 1][j] + a[i][j - 1] + a[i][j + 1]
            print('element=', element)
            new_row.append(element)
        elif i == 0 and j == len(row) - 1 and len(a) != 1 and len(row) != 1:
            element = a[i - 1][j] + a[i + 1][j] + a[i][j - 1] + a[i][j - len(row) + 1]
            print('element=', element)
            new_row.append(element)
        elif i == len(a) - 1 and j != len(row) - 1 and len(a) != 1:
            element = a[i - 1][j] + a[0][j] + a[i][j - 1] + a[i][j + 1]
            print('element=', element)
            new_row.append(element)
        elif i == len(a) - 1 and j == len(row) - 1 and len(a) != 1 and len(row) != 1:
            element = a[i - 1][j] + a[0][j] + a[i][j - 1] + a[i][j - len(row) + 1]
            print('element=', element)
            new_row.append(element)
        elif j == len(row) - 1 and len(a) != 1 and len(row) != 1:
            element = a[i - 1][j] + a[i + 1][j] + a[i][j - 1] + a[i][j - len(row) + 1]
            print('element=', element)
            new_row.append(element)
        elif len(a) == 1 and len(row) == 1:
            element = 4 * a[i][j]
            print('element=', element)
            new_row.append(element)
        elif len(a) == 1:
            element = 2 * a[i][j] + a[i][j - 1] + a[i][j - len(row) + 1]
            print('element=', element)
            new_row.append(element)
        elif len(row) == 1 and i == 0:
            element = a[i - 1][j] + a[i + 1][j] + a[i][j - 1] + a[i][0]
            print('element=', element)
            new_row.append(element)
        elif len(row) == 1 and i != len(a) - 1:
            element = a[i - 1][j] + a[i + 1][j] + a[i][j - 1] + a[i][0]
            print('element=', element)
            new_row.append(element)
        elif len(row) == 1 and i == len(a) - 1:
            element = a[i - 1][j] + a[0][j] + a[i][j - 1] + a[i][0]
            print('element=', element)
            new_row.append(element)
        else:
            element = a[i - 1][j] + a[i + 1][j] + a[i][j - 1] + a[i][j + 1]
            print('element=', element)
            new_row.append(element)
        j += 1
    print('new_row=', new_row)
    b.append(new_row)
    new_row = []
    j = 0

print(b)
for k in b:
    row_b = k
    for k_in in row_b:
        print(k_in, end=' ')
    print()

Оптимальное решение:
c = []
while True:
    a = [i for i in input().split()]
    if a == ['end']:
        break
    c.append(a)
n, m = len(c), len(c[0])
for i in range(n):
    for j in range(m):
        x = int(c[i][j-1]) + int(c[i][j+1-m]) + int(c[i-1][j]) + int(c[i+1-n][j])
        print(x, end=' ')
    print()
'''

'''
Выведите таблицу размером n \times nn×n, заполненную числами от 1 до n^2 
 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
Sample Input:
5
Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

n = int(input())
row = []
mat = []
new = []
k = 1
while k <= n*n:
    for m in range(n):
        row.append(0)
        k += 1
    mat.append(row)
    row = []
k = 1
a = 1
for n1 in range(n//2):
    for j in range(n-a-n1):
        mat[n1][j+n1] = k
        k += 1
    for i in range(n-a-n1):
        mat[i+n1][n-1-n1] = k
        k += 1
    for j in range(n-1-n1, n1, -1):
        mat[n-1-n1][j] = k
        k += 1
    for i in range(n-1-n1, n1, -1):
        mat[i][n1] = k
        k += 1
    a += 1
if n % 2 != 0:
    mat[n//2][n//2] = n*n
for i in mat:
    row = i
    for i_in_row in row:
        print(i_in_row, end=' ')
    print()
print(mat)

Оптимальное решение:
n=int(input())
t=[[0]*n for i in range (n)]
i,j=0,0
for k in range(1, n*n+1):
  t[i][j]=k
  if k==n*n: break
  if i<=j+1 and i+j<n-1: j+=1
  elif i<j and i+j>=n-1: i+=1
  elif i>=j and i+j>n-1: j-=1
  elif i>j+1 and i+j<=n-1: i-=1
for i in range(n):
  print(*t[i])
'''

'''
Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, 
а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка, например:
lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]
lst = [1, 2, 3, 4, 5, 6]
_____________________________________________________________________________________________________________

def modify_list(l):
    i = 0
    while i < len(l):
        if l[i] % 2 == 0:
            l[i] = l[i] // 2
            i += 1
        else:
            del l[i]

print(modify_list(lst))
print(lst)
modify_list(lst)
print(lst)

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)

Оптимальное решение:
def modify_list(l):
    l[:] = [i//2 for i in l if not i % 2]
'''

'''
Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь d и два числа: keykey и valuevalue.

Если ключ keykey есть в словаре dd, то добавьте значение valuevalue в список, который хранится по этому ключу.
Если ключа keykey нет в словаре, то нужно добавить значение в список по ключу 2 * key2∗key. 
Если и ключа 2 * key нет, то нужно добавить ключ 2 * key в словарь и сопоставить ему список из переданного элемента 
[value].
Требуется реализовать только эту функцию, кода вне её не должно быть.
Функция не должна вызывать внутри себя функции input и print.
Пример работы функции:

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}
________________________________________________________________________________________________________________
def update_dictionary(d, key, value):
    if key not in d:
        if 2 * key not in d:
            d[2 * key] = [value]
        else:
            key = 2 * key
            list_value = d[key]
            list_value.append(value)
            d[key] = list_value
    else:
        list_value = d[key]
        list_value.append(value)
        d[key] = list_value


d = {}
key = 2
print(update_dictionary(d, 1, -1))
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)
_________________________________________________________________________________________________________________
Оптимальное решение:
def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    elif 2 * key in d:
        d[2 * key] += [value]
    else:
        d[2 * key] = [value]
'''

'''
Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и 
вывести получившуюся статистику.
Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке 
число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно выводиться только один раз.

Sample Input 1:
a aa abC aa ac abc bcd a
Sample Output 1:
ac 1
a 2
abc 2
bcd 1
aa 2

Sample Input 2:
a A a
Sample Output 2:
a 3
______________________________________________________________________________________________________________________
lst = [i for i in input().split()]
dict_words = {}
for i in lst:
    key = i.lower()
    if key not in dict_words:
        dict_words[key] = 1
    else:
        dict_words[key] += 1
for keys, value in dict_words.items():
    print(keys, value)
______________________________________________________________________________________________________________________
Оптимальное решение:
s = input().lower().split()
for i in set(s):
    print(i, s.count(i))
'''
'''
Напишите программу, которая считывает строку с числом n, которое задаёт количество чисел, которые нужно считать. 
Далее считывает n строк с числами x, по одному числу в каждой строке. Итого будет n+1 строк.
При считывании числа x программа должна на отдельной строке вывести значение f(x). 
Функция f(x) уже реализована и доступна для вызова.
Функция вычисляется достаточно долго и зависит только от переданного аргумента x. 
Для того, чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.

Sample Input:
5
5
12
9
20
12
Sample Output:
11
41
47
61
41
______________________________________________________________________________________________________________________
lst = []
d = {}
n = int(input())
# lst.append(n)
c = 0

while c < n:
    x = int(input())
    lst.append(x)
    c += 1  

for i in lst:
    if i not in d:
        d[i] = f(x)
    print(d[i])

______________________________________________________________________________________________________________________
Оптимальное решение:
# Считайте, что функция f(x) уже определена выше. Определять её отдельно не требуется.
a=[int(input()) for i in range(int(input()))]
b={x:f(x) for x in set(a)}
for i in a:
    print(b[i])
    '''
nums = [4, 3, 2, 7, 8, 2, 3, 1]
i = 0
print(nums)
while i < len(nums):
    pos = nums[i] - 1
    if nums[i] != nums[pos]:
        nums[i], nums[pos] = nums[pos], nums[i]
        print(nums)
    else:
        i += 1

miss = []
for i in range(len(nums)):
    if nums[i] != i + 1:
        miss.append((i+1))
print(miss)
