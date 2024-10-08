"""
Корректные даты
Напишите программу, которая принимает на вход последовательность дат и проверяет каждую из них на корректность.

Формат входных данных
На вход программе подается последовательность дат в формате DD.MM.YYYY, каждая на отдельной строке. Концом
последовательности является слово end.

Формат выходных данных
Программа должна для каждой введенной даты вывести текст Корректная или Некорректная в зависимости от того, является ли
дата корректной, а затем вывести количество корректных дат.

Примечание 1. Для анализа даты на корректность можете использовать уже реализованную функцию is_correct() из предыдущей
задачи.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Таблица форматирования
Sample Input 1:

19.05.2016
05.13.2010
21.12.2012
01.01.1000
32.04.2003
end
Sample Output 1:

Корректная
Некорректная
Корректная
Корректная
Некорректная
3
Sample Input 2:

15.02.1524
29.02.2017
27.05.1528
13.10.1736
40.06.431
31.07.5200
29.02.2016
end
Sample Output 2:

Корректная
Некорректная
Корректная
Корректная
Некорректная
Корректная
Корректная
5
"""
from datetime import date


def is_correct(day: int, month: int, year: int) -> bool:
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False


count = 0

while True:
    inp = input()
    if inp != 'end':
        day, month, year = map(int, inp.split('.'))
        count += is_correct(day, month, year)
        print(['Некорректная', 'Корректная'][is_correct(day, month, year)])
    else:
        print(count)
        break
