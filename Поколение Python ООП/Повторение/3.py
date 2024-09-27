"""
Декоратор @jsonify
Реализуйте декоратор @jsonify, преобразующий возвращаемое значение декорируемой функции в строку формата JSON.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Гарантируется, что возвращаемое значение функции принадлежит типу, который поддерживается форматом JSON.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @jsonify, но не код,
вызывающий его.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

@jsonify
def make_user(id, live, options):
    return {'id': id, 'live': live, 'options': options}

print(make_user(4, False, None))
Sample Output 1:

{"id": 4, "live": false, "options": null}
Sample Input 2:

@jsonify
def make_list(n):
    return list(range(1, n + 1))

print(make_list(10))
Sample Output 2:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Sample Input 3:

@jsonify
def make_str(s1, s2):
    return (s1 + s2) * 5

print(make_str('bee', 'geek'))
Sample Output 3:

"beegeekbeegeekbeegeekbeegeekbeegeek"
"""
from datetime import date, timedelta

y, m = int(input()), int(input())
d = date(y, m, 1)
while d.isoweekday() != 4:
    d = d + timedelta(days=1)
print((d + timedelta(days=21)).strftime('%d.%m.%Y'))
