"""
Напишите функцию func, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает значение
True, если переданный аргумент начинается и заканчивается на английскую букву a (регистр буквы неважен) и False в
противном случае.
"""
func = lambda s: True if s[0] in 'aA' and s[-1] in 'aA' else False
print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))