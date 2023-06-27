"""
Напишите функцию is_num, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает
значение True, если переданный аргумент является числом (целым или вещественным) и False в противном случае.
"""
is_num = lambda x: True if (x.replace('.', '', 1).replace('-', '', 1)).isdigit() and x.startswith('-') \
                           or x.replace('.', '', 1).isdigit() else False
# **********************************************************************************************************************
is_num = lambda x: x.replace('-', '', x[0] == '-').replace('.', '', 1).isdigit()
#x[0]== '-' неявно приводиться к числам 0 или 1

print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))
print(is_num('1-1'))