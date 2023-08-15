"""
FAKE NEWS 🌶️
Команда BEEGEEK планирует выпустить свой новый курс 08.11.2022 ровно в 12:00. Напишите программу, которая принимает на
вход текущие дату и время и определяет, сколько времени осталось до выхода курса.

Формат входных данных
На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.

Формат выходных данных
Программа должна вывести текст с указанием количества дней и часов, оставшихся до выхода курса, в следующем формате:

До выхода курса осталось: <кол-во дней> дней и <кол-во часов> часов
Если в данном случае количество часов равно нулю, то вывести нужно только дни.

Если количество дней равно нулю, то вывести нужно только часы и минуты в следующем формате:

До выхода курса осталось: <кол-во часов> часов и <кол-во минут> минут
Если в данном случае количество минут равно нулю, то вывести нужно только часы. Аналогично, если количество часов равно
нулю, то вывести нужно только минуты.

Если введенные дата и время больше либо равны 08.11.2022 12:00, программа должна вывести текст:

Курс уже вышел!
Примечание 1. Программа должна подбирать правильную форму для существительных «день» и «минута». Для этого можете смело
взять свою функцию choose_plural() из этой задачи.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

16.11.2021 06:30
Sample Output 1:

До выхода курса осталось: 357 дней и 5 часов
Sample Input 2:

06.11.2022 12:00
Sample Output 2:

До выхода курса осталось: 2 дня
Sample Input 3:

08.11.2022 10:30
Sample Output 3:

До выхода курса осталось: 1 час и 30 минут
Sample Input 4:

08.11.2022 09:00
Sample Output 4:

До выхода курса осталось: 3 часа
Sample Input 5:

08.11.2022 11:40
Sample Output 5:

До выхода курса осталось: 20 минут
Sample Input 6:

08.11.2022 12:15
Sample Output 6:

Курс уже вышел!
"""
from datetime import datetime, timedelta


def choose_plural(amount: int, dec: tuple) -> str:
    if int(str(amount)[-1]) == 1 and int(str(amount)[-2:]) != 11:
        return f'{amount} {dec[0]}'
    elif int(str(amount)[-1]) in (2, 3, 4) and int(str(amount)[-2:]) not in range(5, 21):
        return f'{amount} {dec[1]}'
    return f'{amount} {dec[2]}'


def hours_minutes(td):
    return td.seconds // 3600, (td.seconds // 60) % 60


pattern = '%d.%m.%Y %H:%M'
production = datetime.strptime('08.11.2022 12:00', pattern)
now = datetime.strptime(input(), pattern)

timer = production - now
hours, minutes = hours_minutes(timer)

dec_day = ('день', 'дня', 'дней')
dec_hours = ('час', 'часа', 'часов')
dec_minute = ('минута', 'минуты', 'минут')

if timer.days and timer.total_seconds() > 0:
    if hours != 0:
        print(f'До выхода курса осталось: {choose_plural(timer.days, dec_day)} и {choose_plural(hours, dec_hours)}')
    else:
        print(f'До выхода курса осталось: {choose_plural(timer.days, dec_day)}')
elif now >= production:
    print('Курс уже вышел!')
else:
    if minutes == 0:
        print('До выхода курса осталось:', choose_plural(hours, dec_hours))
    elif hours == 0:
        print('До выхода курса осталось:', choose_plural(minutes, dec_minute))
    else:
        print('До выхода курса осталось:', choose_plural(hours, dec_hours), 'и', choose_plural(minutes, dec_minute))


# ********************************************************************************************************************
"""
Сыпется при входных данных 07.11.2022 11:30.
Будет выведено 'До выхода курса осталось: 1 день и 30 минут', а по условию требуется выводить в таком случае только дни.
"""

def strp(d):
    rv = []
    mins = int(d.total_seconds() // 60)
    tuples = (24 * 60, ('день', 'дня', 'дней')), (60, ('час', 'часа', 'часов')), (1, ('минута', 'минуты', 'минут'))
    for n, f in tuples:
        if mins // n:
            rv.append(choose_plural(mins // n, f))
        mins = mins % n
    return ' и '.join(rv[:2])


delta = datetime(2022, 11, 8, 12) - datetime.strptime(input(), '%d.%m.%Y %H:%M')

print('Курс уже вышел!' if delta <= timedelta() else 'До выхода курса осталось: ' + strp(delta))