"""
Функция number_of_frogs()
В первый год в пруду живет
77
77 лягушек. Каждый год из пруда вылавливают
30
30 лягушек, а оставшиеся размножаются, и их становится в три раза больше. Так, количество лягушек
�
k-й год  может быть описано формулой:

�
�
=
3
(
�
�
−
1
−
30
)
F
k
​
 =3(F
k−1
​
 −30)

Реализуйте функцию number_of_frogs() с использованием рекурсии, которая принимает один аргумент:

year — натуральное число
Функция должна возвращать единственное число — количество лягушек в пруду в году year.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию number_of_frogs(), но не
код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(number_of_frogs(2))
Sample Output 1:

141
Sample Input 2:

print(number_of_frogs(10))
Sample Output 2:

629901
Sample Input 3:

print(number_of_frogs(1))
Sample Output 3:

77
"""


def number_of_frogs(y):
    if y == 1:
        return 77
    return 3 * (number_of_frogs(y - 1) - 30)


print(number_of_frogs(10))