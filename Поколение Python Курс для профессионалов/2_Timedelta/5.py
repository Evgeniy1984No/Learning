"""
Функция num_of_sundays()
Реализуйте функцию num_of_sundays(), которая принимает на вход один аргумент:

year — натуральное число, год
Функция должна возвращать количество воскресений в году year.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию num_of_sundays(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(num_of_sundays(2021))
Sample Output 1:

52
Sample Input 2:

year = 2000
print(num_of_sundays(year))
Sample Output 2:

53
Sample Input 3:

print(num_of_sundays(768))
Sample Output 3:

52
"""
from datetime import timedelta, date, datetime


def num_of_sundays(year: int) -> int:
    start = date(year=year, month=1, day=1)
    start = start + timedelta(days=6-start.weekday())
    end = date(year=year, month=12, day=31)
    return (end - start).days // 7 + 1


# ********************************************************************************************************************
# Количество воскресений в году равно номеру недели, начинающейся с воскресенья, для 31 декабря (%U)
def num_of_sundays_best(year):
    dt = datetime(year, 12, 31)
    return dt.strftime('%U')


print(num_of_sundays_best(2021))
print(num_of_sundays(2000))
print(num_of_sundays(768))