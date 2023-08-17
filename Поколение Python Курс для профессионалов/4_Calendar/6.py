"""
Функция get_all_mondays()
Реализуйте функцию get_all_mondays(), которая принимает один аргумент:

year — натуральное число
Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) года year, выпадающих на
понедельник.

Примечание 1. Например, вызов:

get_all_mondays(2021)
должен вернуть список:

[datetime.date(2021, 1, 4), datetime.date(2021, 1, 11), ..., datetime.date(2021, 12, 20), datetime.date(2021, 12, 27)]
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_all_mondays(), но не
код, вызывающий ее.
"""
import calendar
from datetime import date


def get_all_mondays(year) -> list:
    monday_caledar = []
    for month in range(1, 13):
        [monday_caledar.append(date(year, month, j[0])) for j in calendar.monthcalendar(year, month) if j[0]]
    return monday_caledar


print(get_all_mondays(2021))