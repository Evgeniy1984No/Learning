"""
Корпоративная почта 🌶️
В онлайн-школе "BEEGEEK" сотрудникам положена корпоративная почта, которая формируется как <имя-фамилия>@beegeek.bzz,
например, timyr-guev@beegeek.bzz. При таком подходе существует проблема тёзок. Для решения такой проблемы было решено
приписывать справа номер.

Тогда первый Тимур Гуев получает ящик timyr-guev@beegeek.bzz (без номера), второй — timyr-guev1@beegeek.bzz, третий —
timyr-guev2@beegeek.bzz, и так далее.

Вам дан список уже занятых ящиков в порядке их выдачи и имена-фамилии новых сотрудников в заранее подготовленном виде
(латиницей с символом - между ними). Напишите программу, которая раздает корпоративные ящики новым сотрудникам школы.

Формат входных данных
На вход программе в первой строке подается целое неотрицательное число
�
n — количество выданных ящиков. В следующих
�
n строках перечислены сами ящики в порядке выдачи, по одному на строке. На следующей строке задано целое неотрицательное
число
�
m — количество новых сотрудников, которым нужно раздать корпоративные ящики. Каждая из последующих
�
m строк представляет собой имя и фамилию сотрудника в подготовленном к использованию формате.

Формат выходных данных
Программа должна вывести почтовые ящики (
�
m строк) для новых сотрудников в том порядке, в котором они раздавались.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

6
ivan-petrov@beegeek.bzz
petr-ivanov@beegeek.bzz
ivan-petrov1@beegeek.bzz
ivan-ivanov@beegeek.bzz
ivan-ivanov1@beegeek.bzz
ivan-ivanov2@beegeek.bzz
3
ivan-ivanov
petr-petrov
petr-ivanov
Sample Output 1:

ivan-ivanov3@beegeek.bzz
petr-petrov@beegeek.bzz
petr-ivanov1@beegeek.bzz
Sample Input 2:

2
timyr-guev2@beegeek.bzz
anri-tabuev@beegeek.bzz
3
timyr-guev
timyr-guev
anri-tabuev
Sample Output 2:

timyr-guev@beegeek.bzz
timyr-guev1@beegeek.bzz
anri-tabuev1@beegeek.bzz
"""

old_mail = sorted(list(map(lambda x: x[:x.index('@')], [input() for _ in range(int(input()))])))
new_mail = [input() for _ in range(int(input()))]


def check_mail(name: str, list_mail: list, num='') -> str:
    if name + num in list_mail:
        if num.isdigit():
            num = str(int(num) + 1)
        else:
            num = '1'
        return check_mail(name, list_mail, num)
    else:
        list_mail.append(name + num)
        return name + num


[print(check_mail(name, old_mail) + '@beegeek.bzz') for name in new_mail]
# **************************************************************************************************************
emails = set(input() for _ in range(int(input())))
for _ in range(int(input())):
    emp = input()
    email = f'{emp}@beegeek.bzz'
    count = 0
    while email in emails:
        count += 1
        email = f'{emp}{count}@beegeek.bzz'
    emails.add(email)
    print(email)