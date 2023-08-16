"""
Функция get_the_fastest_func()
Реализуйте функцию get_the_fastest_func(), которая принимает два аргумента в следующем порядке:

funcs — список произвольных функций
arg — произвольный объект
Функция get_the_fastest_func() должна возвращать функцию из списка funcs, которая затратила на вычисление значения при
вызове с аргументом arg наименьшее количество времени.

Примечание. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_the_fastest_func(), но не
код, вызывающий ее.
"""
import time


def calculate_it(func, *args):
    start = time.monotonic()
    func(*args)
    end = time.monotonic()
    return func, end - start


def get_the_fastest_func(funcs: list, arg):
    times = []
    for f in funcs:
        times.append(calculate_it(f, arg))
    return min(times, key=lambda x: x[1])[0]


def slow(arg):
    time.sleep(3)


def fast(arg):
    time.sleep(1)


funcs = [slow, fast]

print(get_the_fastest_func(funcs, 0))