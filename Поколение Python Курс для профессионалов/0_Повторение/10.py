"""
Функция get_biggest() 🌶️🌶️
Реализуйте функцию get_biggest(), которая принимает один аргумент:

numbers — список целых неотрицательных чисел
Функция должна возвращать наибольшее число, которое можно составить из чисел из списка numbers. Если список numbers
пуст, функция должна вернуть число
−
1
−1.

Примечание 1. Рассмотрим первый тест со списком чисел [1, 2, 3], из которых можно составить следующие числа:
123
,
132
,
213
,
231
,
312
,
321
123,132,213,231,312,321
Наибольшим из представленных является
321
321.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_biggest(), но не код,
вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(get_biggest([1, 2, 3]))
Sample Output 1:

321
Sample Input 2:

print(get_biggest([61, 228, 9, 3, 11]))
Sample Output 2:

961322811
Sample Input 3:

print(get_biggest([71, 7, 72]))
Sample Output 3:

77271
Sample Input 4:

print(get_biggest([]))
Sample Output 4:

-1

[7, 87, 86, 344]
[87, 86, 344]
78786344
87867344
"""


def get_biggest(numbers: list) -> int:
    if numbers:
        lst_sort = (sorted(numbers, key=lambda x: str(x) * max(numbers, key=lambda y: len(str(y))), reverse=True))
        return int(''.join(map(str, lst_sort)))
    return -1


print(get_biggest([7, 87, 86, 344]))
