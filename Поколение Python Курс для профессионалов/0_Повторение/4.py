"""
Функция convert()
Реализуйте функцию convert(), которая принимает один аргумент:

string — произвольная строка
Функция должна возвращать строку string:

полностью в нижнем регистре, если букв в нижнем регистре в этой строке больше
полностью в верхнем регистре, если букв в верхнем регистре в этой строке больше
полностью в нижнем регистре, если количество букв в верхнем и нижнем регистрах в этой строке совпадает
Примечание 1. Символы строки, не являющиеся буквами, следует игнорировать.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию convert(), но не код,
вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(convert('BEEgeek'))
Sample Output 1:

beegeek
Sample Input 2:

print(convert('pyTHON'))
Sample Output 2:

PYTHON
Sample Input 3:

print(convert('pi31415!'))
Sample Output 3:

pi31415!
"""


def convert(string: str) -> str:
    lst_alpha = [char for char in string if char.isalpha()]
    len_lower = sum([i.islower() for i in lst_alpha])
    if len_lower >= len(lst_alpha) // 2:
        return string.lower()
    else:
        return string.upper()


print(convert('BEEgeek'))
print(convert('pyTHON'))
print(convert('pi31415!'))
# *******************************************************************************************************************


def convert_1(string):
    if sum(1 if c.isupper() else -1 for c in string if c.isalpha()) > 0:
        return string.upper()
    return string.lower()