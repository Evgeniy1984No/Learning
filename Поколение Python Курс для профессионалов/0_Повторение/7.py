"""
Функция index_of_nearest()
Реализуйте функцию index_of_nearest(), которая принимает два аргумента в следующем порядке:

numbers — список целых чисел
number — целое число
Функция должна находить в списке numbers ближайшее по значению число к числу number и возвращать его индекс. Если список
numbers пуст, функция должна вернуть число
−
1
−1.

Примечание 1. Если в функцию передается список, содержащий несколько чисел, одновременно являющихся ближайшими к
искомому числу, функция должна возвращать наименьший из индексов ближайших чисел.

Примечание 2. Рассмотрим третий тест. Ближайшими числами к числу
4
4 являются
5
5 и
3
3, имеющие индексы
1
1 и
2
2 соответственно. Наименьший из индексов равен
1
1.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию index_of_nearest(), но не
код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(index_of_nearest([], 17))
Sample Output 1:

-1
Sample Input 2:

print(index_of_nearest([7, 13, 3, 5, 18], 0))
Sample Output 2:

2
Sample Input 3:

print(index_of_nearest([9, 5, 3, 2, 11], 4))
Sample Output 3:

1
Sample Input 4:

print(index_of_nearest([7, 5, 4, 4, 3], 4))
Sample Output 4:

2
"""


def index_of_nearest(numbers: list, number: int) -> int:
    if len(numbers) == 0:
        return -1
    ind = 0
    temp = abs(numbers[0] - number)
    for i in range(len(numbers)):
        if abs(numbers[i] - number) < temp:
            temp = abs(numbers[i] - number)
            ind = i
    return ind


print(index_of_nearest([], 17))
print(index_of_nearest([7, 5, 4, 4, 3], 4))
print(index_of_nearest([7, 13, 3, 5, 18], 0))
# *************************************************************************************************************


def index_of_nearest_1(nums, n):
    if nums:
        minimum = min(nums, key=lambda num: abs(num - n))
        return nums.index(minimum)
    return -1