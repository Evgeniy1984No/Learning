"""
На вход программе подается Decimal число
�
d. Напишите программу, которая вычисляет значение выражения:
(e)^d+ln(d)+lg(d)+d^0.5
"""
from decimal import *
d = Decimal(input())
res = d.exp() + d.ln() + d.log10() + d.sqrt()
print(res)