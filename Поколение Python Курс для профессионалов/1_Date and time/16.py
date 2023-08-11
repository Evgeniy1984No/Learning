"""
Функция is_available_date() 🌶️
Во время визита очередного гостя сотрудникам отеля приходится проверять, доступна ли та или иная дата для бронирования
номера.

Реализуйте функцию is_available_date(), которая принимает два аргумента в следующем порядке:

booked_dates — список строковых дат, недоступных для бронирования. Элементом списка является либо одиночная дата, либо
период (две даты через дефис). Например:
['04.11.2021', '05.11.2021-09.11.2021']
date_for_booking — одиночная строковая дата или период (две даты через дефис), на которую гость желает забронировать
номер. Например:
'01.11.2021' или '01.11.2021-04.11.2021'
Функция is_available_date() должна возвращать True, если дата или период date_for_booking полностью доступна для
бронирования. В противном случае функция должна возвращать False.

Примечание 1. Гарантируется, что в периоде левая дата всегда меньше правой.

Примечание 2. В периоде (две даты через дефис) граничные даты включены.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_available_date(), но не
код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))
Sample Output 1:

True
Sample Input 2:

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))
Sample Output 2:

False
Sample Input 3:

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'
print(is_available_date(dates, some_date))
Sample Output 3:

False
"""
from datetime import datetime

pattern = '%d.%m.%Y'


def is_available_date(booked_dates: list, date_for_booking: str) -> bool:
    def get_dates_rage(date_range: str) -> set:
        set_out = []
        if '-' in date_range:
            start, end = date_range.split('-')
            start = datetime.strptime(start, pattern)
            end = datetime.strptime(end, pattern)
            set_out.extend([datetime.fromordinal(i).date() for i in range(start.toordinal(), end.toordinal() + 1)])
        else:
            set_out.append(datetime.strptime(date_range, pattern).date())
        return set(set_out)

    booked_dates_set = set()
    for d in booked_dates:
        booked_dates_set.update(get_dates_rage(d))
    date_for_booking_set = get_dates_rage(date_for_booking)
    return date_for_booking_set.isdisjoint(booked_dates_set)


dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'
print(is_available_date(dates, some_date))
