"""
Функция is_power()
Реализуйте функцию is_power() с использованием рекурсии, которая принимает один аргумент:

number — натуральное число
Функция должна возвращать значение True, если number является степенью числа
2
2, или False в противном случае.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_power(), но не код,
вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(is_power(512))
Sample Output 1:

True
Sample Input 2:

print(is_power(15))
Sample Output 2:

False
Sample Input 3:

print(is_power(1))
Sample Output 3:

True
"""


def is_power(number):
    if number == 1:
        return True
    elif number % 2 == 0:
        return is_power(number // 2)
    else:
        return False
