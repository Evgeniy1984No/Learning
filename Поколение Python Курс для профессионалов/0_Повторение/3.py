"""
Функция is_valid()
Будем считать, что PIN-код является корректным, если он удовлетворяет следующим условиям:

состоит из
4
4,
5
5 или
6
6 символов
состоит только из цифр (
0
−
9
0−9)
не содержит пробелов
Реализуйте функцию is_valid(), которая принимает один аргумент:

string — произвольная строка
Функция должна возвращать значение True, если строка string представляет собой корректный PIN-код, или False в противном
случае.

Примечание 1. Если в функцию передается пустая строка, функция должна возвращать значение False.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_valid(), но не код,
вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(is_valid('4367'))
Sample Output 1:

True
Sample Input 2:

print(is_valid('92134'))
Sample Output 2:

True
Sample Input 3:

print(is_valid('89abc1'))
Sample Output 3:

False
Sample Input 4:

print(is_valid('900876'))
Sample Output 4:

True
Sample Input 5:

print(is_valid('49 83'))
Sample Output 5:

False
"""


def is_valid(string):
    return string.isdigit() and len(string) in range(4, 7)


print(is_valid('4367'))
print(is_valid('89abc1'))
print(is_valid('49 83'))