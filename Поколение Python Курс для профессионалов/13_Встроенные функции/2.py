"""
Функция non_negative_even()
Реализуйте функцию non_negative_even(),  которая принимает один аргумент:

numbers — непустой список чисел
Функция должна возвращать True, если все числа в списке numbers являются четными и неотрицательными, или False в
противном случае.

Примечание 1. В задаче удобно воспользоваться функцией all().

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию non_negative_even(), но не
код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(non_negative_even([0, 2, 4, 8, 16]))
Sample Output 1:

True
Sample Input 2:

print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))
Sample Output 2:

False
Sample Input 3:

print(non_negative_even([0, 0, 0, 0, 0]))
Sample Output 3:

True
"""


def non_negative_even(numbers: list) -> bool:
    return all(num >= 0 and num % 2 == 0 for num in numbers)


print(non_negative_even([0, 2, 4, 8, 16]))
print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))
print(non_negative_even([0, 0, 0, 0, 0]))
