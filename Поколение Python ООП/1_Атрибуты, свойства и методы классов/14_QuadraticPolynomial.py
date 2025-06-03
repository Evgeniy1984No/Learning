"""
Класс QuadraticPolynomial
Квадратный трехчлен — это многочлен вида
a
x
2
+
b
x
+
c
ax
2
 +bx+c, где
a
≠
0
a

=0. Например:
x
2
+
1
x
2
−
5
x
+
6
x
2
 +1
x
2
 −5x+6
Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен. При создании экземпляра класс должен принимать
три аргумента в следующем порядке:

a — коэффициент
a
a квадратного трехчлена
b — коэффициент
b
b квадратного трехчлена
c — коэффициент
c
c квадратного трехчлена
Экземпляр класса QuadraticPolynomial должен иметь три атрибута:

a — коэффициент
a
a квадратного трехчлена
b — коэффициент
b
b квадратного трехчлена
c — коэффициент
c
c квадратного трехчлена
Класс QuadraticPolynomial должен иметь два метода класса:

from_iterable() — метод, принимающий в качестве аргумента итерируемый объект из трех элементов a, b и c, которые
представляют коэффициенты квадратного трехчлена, и возвращающий экземпляр класса QuadraticPolynomial, созданный
на основе переданных коэффициентов
from_str() — метод, принимающий в качестве аргумента строку, которая содержит коэффициенты a, b и c квадратного
трехчлена, записанные через пробел. Метод должен возвращать экземпляр класса QuadraticPolynomial, созданный на
основе переданных коэффициентов, предварительно преобразованных в экземпляры класса float
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

polynom = QuadraticPolynomial(1, -5, 6)

print(polynom.a)
print(polynom.b)
print(polynom.c)
Sample Output 1:

1
-5
6
Sample Input 2:

polynom = QuadraticPolynomial.from_iterable([2, 13, -1])

print(polynom.a)
print(polynom.b)
print(polynom.c)
Sample Output 2:

2
13
-1
Sample Input 3:

polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')

print(polynom.a)
print(polynom.b)
print(polynom.c)
print(polynom.a + polynom.b + polynom.c)
Sample Output 3:

-1.5
4.0
14.8
"""


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, seq):
        a, b, c = seq
        return cls(a, b, c)

    @classmethod
    def from_str(cls, s):
        a, b, c = map(float, s.split())
        return cls(a, b, c)