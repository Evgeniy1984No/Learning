"""
Функция polynom()
Реализуйте функцию polynom(), которая принимает один аргумент:

x — вещественное число
Функция должна возвращать значение выражения
�
2
+
1
x
2
 +1.

Также функция должна иметь атрибут values, представляющий собой множество (тип set) всех значений функции, которые
уже были вычислены.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию polynom(), но не код,
вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(polynom(5))
print(polynom.values)
Sample Output 1:

26
{26}
Sample Input 2:

polynom(1)
polynom(2)
polynom(3)

print(*sorted(polynom.values))
Sample Output 2:

2 5 10
Sample Input 3:

for _ in range(10):
    polynom(10)

print(polynom.values)
Sample Output 3:

{101}
"""


def polynom(x):
    res = x**2 + 1
    polynom.__dict__.setdefault('values', set()).add(res)
    return res


print(polynom(5))
print(polynom.values)
polynom(1)
polynom(2)
polynom(3)
print(*sorted(polynom.values))