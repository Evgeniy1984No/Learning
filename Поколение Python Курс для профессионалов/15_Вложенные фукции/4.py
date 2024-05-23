"""
Функция sort_priority() 🌶️
Реализуйте функцию sort_priority(), которая принимает два аргумента в следующем порядке:

values — список чисел
group — список, кортеж или множество чисел
Функция должна сортировать по неубыванию список чисел values, делая при этом приоритетной группу чисел из group,
которая должна следовать первой.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию sort_priority(), но не
код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)

print(numbers)
Sample Output 1:

[2, 3, 5, 7, 1, 4, 6, 8]
Sample Input 2:

numbers = [150, 200, 300, 1000, 50, 20000]
sort_priority(numbers, [300, 100, 200])

print(numbers)
Sample Output 2:

[200, 300, 50, 150, 1000, 20000]
Sample Input 3:

numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
sort_priority(numbers, (300, 100, 200))

print(numbers)
Sample Output 3:

[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


def sort_priority(values, group):
    lst = []
    for elem in sorted(group):
        if elem in values:
            values.remove(elem)
            lst.append(elem)
    values[:] = lst + sorted(values)
    return values


# *******************************************************************************************************************
def sort_priority(numbers, group):
    numbers.sort(key=lambda x: (x not in group, x))


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
print(sorted(group) + sorted(numbers))
# sort_priority(numbers, group)
# print(numbers)

numbers = [150, 200, 300, 1000, 50, 20000]
sort_priority(numbers, [300, 100, 200])
print(numbers)

numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
sort_priority(numbers, (300, 100, 200))
print(numbers)