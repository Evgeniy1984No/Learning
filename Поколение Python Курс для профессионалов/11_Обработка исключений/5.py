"""
Функция get_weekday()
Реализуйте функцию get_weekday(), которая принимает один аргумент:

number — целое число (от
1
1 до
7
7 включительно)
Функция должна возвращать полное название дня недели на русском, который соответствует числу number, при этом:

если number не является целым числом, функция должна возбуждать исключение:
TypeError('Аргумент не является целым числом')
если number является целым числом, но не принадлежит отрезку
[
1
;
7
]
[1;7], функция должна возбуждать исключение:
ValueError('Аргумент не принадлежит требуемому диапазону')
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_weekday(), но не код,
вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(get_weekday(1))
Sample Output 1:

Понедельник
Sample Input 2:

try:
    print(get_weekday('hello'))
except Exception as err:
    print(err)
    print(type(err))
Sample Output 2:

Аргумент не является целым числом
<class 'TypeError'>
Sample Input 3:

try:
    print(get_weekday(8))
except ValueError as err:
    print(err)
    print(type(err))
Sample Output 3:

Аргумент не принадлежит требуемому диапазону
<class 'ValueError'>
"""
import calendar, locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


def get_weekday(number: int):
    if type(number) != int:
        raise TypeError('Аргумент не является целым числом')
    elif number not in range(1, 8):
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    return calendar.day_name[number - 1].capitalize()



