"""
Сопряженные числа
Дано натуральное число n и два комплексных числа z1, z2.

Напишите программу, которая вычисляет и выводит значение выражения
z1^n +z2^n +|z1^n + |z2^n+1
Тестовые данные 🟢
Sample Input 1:

1
2+3j
1+4j
Sample Output 1:

(-10-4j)
Sample Input 2:

2
2+3j
1+4j
Sample Output 2:

(-72+60j)
"""
n = int(input())
z1, z2 = complex(input()), complex(input())
print(z1**n + z2**n + (z1.conjugate())**n + (z2.conjugate())**(n+1))