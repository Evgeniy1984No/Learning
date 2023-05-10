"""
Дополните приведенный код, чтобы он вывел сумму наибольшей и наименьшей цифры Decimal числа.
"""
from decimal import *
num = Decimal(input())
digs = num.as_tuple().digits
print((min(digs) + max(digs)) if num.as_tuple().exponent * (-1) < len(digs) else max(digs))
# ******************************************************************************************************************
print(max(digs) + min(digs) * (abs(num) >= 1))