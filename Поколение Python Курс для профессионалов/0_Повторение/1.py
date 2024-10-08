"""
Функция same_parity()
Реализуйте функцию same_parity(), которая принимает один аргумент:

numbers — список целых чисел
Функция должна возвращать новый список, элементами которого являются числа из списка numbers, имеющие ту же четность,
что и первый элемент этого списка.

Примечание 1. Числа в возвращаемом функцией списке должны располагаться в своем исходном порядке.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию same_parity(), но не код,
вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(same_parity([]))
Sample Output 1:

[]
Sample Input 2:

print(same_parity([6, 0, 67, -7, 10, -20]))
Sample Output 2:

[6, 0, 10, -20]
Sample Input 3:

print(same_parity([-7, 0, 67, -9, 70, -29, 90]))
Sample Output 3:

[-7, 67, -9, -29]
"""


def same_parity(numbers: list) -> list:
    return list(filter(lambda x: x % 2 == numbers[0] % 2, numbers))


# **********************************************************************************************************************
def same_parity_1(nums):
    return [i for i in nums if i % 2 == nums[0] % 2]
