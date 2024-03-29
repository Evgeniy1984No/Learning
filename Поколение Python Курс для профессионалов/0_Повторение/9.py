"""
Функция choose_plural() 🌶️🌶️
Реализуйте функцию choose_plural(), которая принимает два аргумента в следующем порядке:

amount — натуральное число, количество
declensions — кортеж из трех вариантов склонения существительного
Функция должна возвращать строку, полученную путем объединения подходящего существительного из кортежа declensions и
количества amount, в следующем формате:

<количество> <существительное>
Примечание 1. Передаваемый в функцию кортеж легко составить по мнемоническому правилу: один, два, пять. Например:

для слова «арбуз»: арбуз, арбуза, арбузов
для слова «рубль»: рубль, рубля, рублей
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию choose_plural(), но не код,
вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(choose_plural(21, ('пример', 'примера', 'примеров')))
Sample Output 1:

21 пример
Sample Input 2:

print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
Sample Output 2:

92 гвоздя
Sample Input 3:

print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
Sample Output 3:

8 яблок
"""


def choose_plural(amount: int, dec: tuple) -> str:
    if int(str(amount)[-1]) == 1 and int(str(amount)[-2:]) != 11:
        return f'{amount} {dec[0]}'
    elif int(str(amount)[-1]) in (2, 3, 4) and int(str(amount)[-2:]) not in range(5, 21):
        return f'{amount} {dec[1]}'
    return f'{amount} {dec[2]}'


print(choose_plural(21, ('пример', 'примера', 'примеров')))
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
print(choose_plural(322, ('цент', 'цента', 'центов')))
print(choose_plural(11, ('стул', 'стула', 'стульев')))