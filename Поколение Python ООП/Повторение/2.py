"""
Функция inversions()
Дана последовательность чисел
a
1
,
a
2
,
.
.
.
,
a
n
a
1
​
 ,a
2
​
 ,...,a
n
​
 . Назовем пару
(
a
i
,
a
j
)
(a
i
​
 ,a
j
​
 ) инверсией, если
i
<
j
i<j, а
a
i
>
a
j
a
i
​
 >a
j
​
 . Например, последовательность
3
,
1
,
4
,
2
3,1,4,2 имеет три инверсии
(
3
,
1
)
,
(
3
,
2
)
,
(
4
,
2
)
(3,1),(3,2),(4,2). Каждая инверсия — это пара элементов, нарушающих порядок.

Реализуйте функцию inversions(), которая принимает один аргумент:

sequence — последовательность, элементами которой являются числа
Функция должна возвращать единственное число — количество инверсий в последовательности sequence.

Примечание 1. Последовательностью будем считать объект, имеющий длину и поддерживающий индексацию. Например, объекты
типа list или range являются последовательностями.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию inversions(), но не код,
вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

sequence = [3, 1, 4, 2]

print(inversions(sequence))
Sample Output 1:

3
Sample Input 2:

sequence = [1, 2, 3, 4, 5]

print(inversions(sequence))
Sample Output 2:

0
Sample Input 3:

sequence = [4, 3, 2, 1]

print(inversions(sequence))
Sample Output 3:

6
Sample Input 4:

sequence = [1, 1, 1, 1, 1, 1]

print(inversions(sequence))
Sample Output 4:

0
"""
import sys


d = set()
s = 0
for line in sys.stdin:
    if line in d:
        s += 1
    else:
        d.add(line)
print(s)
