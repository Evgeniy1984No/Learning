"""
Функция print_given()
Реализуйте функцию print_given(), которая принимает произвольное количество позиционных и именованных аргументов и
выводит все переданные аргументы, указывая тип каждого. Пары аргумент-тип должны выводиться каждая на отдельной строке,
в следующем формате:

для позиционных аргументов:
<значение аргумента> <тип аргумента>
для именованных аргументов:
<имя переменной> <значение аргумента> <тип аргумента>
Примечание 1. При выводе позиционные аргументы должны быть расположены в порядке их передачи, именованные — в
лексикографическом порядке имен переменных.

Примечание 2. При выводе сначала должны следовать все позиционные аргументы, затем — все именованные.

Примечание 3. Если в функцию ничего не передается, функция ничего не должна выводить.

Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимую функцию print_given(), но не код,
вызывающий ее.

Примечание 5. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print_given(1, [1, 2, 3], 'three', two=2)
Sample Output 1:

1 <class 'int'>
[1, 2, 3] <class 'list'>
three <class 'str'>
two 2 <class 'int'>
Sample Input 2:

print_given('apple', 'cherry', 'watermelon')
Sample Output 2:

apple <class 'str'>
cherry <class 'str'>
watermelon <class 'str'>
Sample Input 3:

print_given(b=2, d=4, c=3, a=1)
Sample Output 3:

a 1 <class 'int'>
b 2 <class 'int'>
c 3 <class 'int'>
d 4 <class 'int'>
Sample Input 4:

print_given()
Sample Output 4:
"""


def print_given(*args, **kwargs):
    [print(f'{arg} {type(arg)}') for arg in args]
    [print(f'{key} {value} {type(value)}') for key, value in sorted(kwargs.items())]


print_given()
