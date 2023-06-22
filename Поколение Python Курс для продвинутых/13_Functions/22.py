"""
Напишите функцию func, используя синтаксис анонимных функций, которая принимает целочисленный аргумент и возвращает
значение True, если он делится без остатка на
19
19 или на
13
13 и False в противном случае.

Примечание 1. Следующий программный код:

print(func(19))
print(func(13))
print(func(20))
print(func(15))
print(func(247))
должен выводить:

True
True
False
False
True
"""
func = lambda x: True if x % 19 == 0 or x % 13 == 0 else False
print(func(19))
print(func(13))
print(func(20))
print(func(15))
print(func(247))