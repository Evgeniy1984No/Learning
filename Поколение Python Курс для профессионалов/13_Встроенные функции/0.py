"""
Функция convert()
Реализуйте функцию convert(), которая принимает один аргумент:

number — целое число
Функция должна возвращать кортеж из трех элементов, расположенных в следующем порядке:

двоичное представление числа number в виде строки без префикса 0b
восьмеричное представление числа number в виде строки без префикса 0o
шестнадцатеричное представление числа number в виде строки в верхнем регистре без префикса 0x
Примечание 1. В задаче удобно воспользоваться функциями bin(), oct() и hex().

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию convert(), но не код,
вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(convert(15))
Sample Output 1:

('1111', '17', 'F')
Sample Input 2:

print(convert(-24))
Sample Output 2:

('-11000', '-30', '-18')
Sample Input 3:

print(convert(1))
Sample Output 3:

('1', '1', '1')
"""


# def convert(number):
#     res = list(map(str, [bin(number), oct(number), hex(number)]))
#
#     def str_convert(string):
#         if string[0] == '-':
#             return '-' + string[3:].upper()
#         return string[2:].upper()
#
#     res = tuple(map(str_convert, res))
#     return res

def convert(n):
    return f'{n:b}', f'{n:o}', f'{n:X}'


print(convert(15))
print(convert(-24))