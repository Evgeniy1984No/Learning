"""
Декоратор exception_decorator
Реализуйте декоратор exception_decorator, который возвращает

кортеж (value, 'Функция выполнилась без ошибок'), если декорируемая функция завершила свою работу без ошибок, где value
 — возвращаемое значение декорируемой функции
кортеж (None, 'При вызове функции произошла ошибка'), если при выполнении декорируемой функции возникла ошибка

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор exception_decorator,
но не код, вызывающий его.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

@exception_decorator
def f(x):
    return x**2 + 2*x + 1

print(f(7))
Sample Output 1:

(64, 'Функция выполнилась без ошибок')
Sample Input 2:

sum = exception_decorator(sum)

print(sum(['199', '1', 187]))
Sample Output 2:

(None, 'При вызове функции произошла ошибка')
"""


def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs), 'Функция выполнилась без ошибок'
        except:
            return None, 'При вызове функции произошла ошибка'
    return wrapper


@exception_decorator
def f(x):
    return x**2 + 2*x + 1

print(f(7))


sum = exception_decorator(sum)

print(sum(['199', '1', 187]))

