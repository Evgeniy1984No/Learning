"""
В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней,
равное days.

Примечание:
Для решения этой задачи используйте стандартный модуль datetime.
Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta для прибавления дней к дате.

Sample Input 1:

2016 4 20
14
Sample Output 1:

2016 5 4
Sample Input 2:

2016 2 20
9
Sample Output 2:

2016 2 29
Sample Input 3:

2015 12 31
1
Sample Output 3:

2016 1 1
"""

from datetime import timedelta, datetime


def whatisdate():
    date = datetime.strptime(input('Enter date(year, month, day): '), "%Y %m %d")
    date += timedelta(days=int(input('Enter days: ')))
    print(date.year, date.month, date.day)
    return


# whatisdate()

"""
_______________________________________________________________________________________________________________________
"""

inp = datetime.strptime(input(), "%Y %m %d")
inp += timedelta(days=int(input()))
print(f'{inp.year} {inp.month} {inp.day}')
