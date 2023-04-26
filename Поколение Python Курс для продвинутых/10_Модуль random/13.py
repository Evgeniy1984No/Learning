"""
Генератор паролей 2 🌶️
Напишите программу, которая с помощью модуля random генерирует
�
n паролей длиной
�
m символов, состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:

«l» (L маленькое);
«I» (i большое);
«1» (цифра);
«o» и «O» (большая и маленькая буквы);
«0» (цифра).
Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра и как минимум по одной
букве в верхнем и нижнем регистре.

Формат входных данных
На вход программе подаются два числа
�
n и
�
m, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести
�
n паролей длиной
�
m символов в соответствии с условием задачи, каждый на отдельной строке.

Примечание 1. Считать, что числа
�
n и
�
m всегда таковы, что требуемые пароли сгенерировать возможно.

Примечание 2. Решение задачи удобно оформить в виде двух вспомогательных функций:

функция generate_password(length) – возвращает случайный пароль длиной length символов;
функция generate_passwords(count, length) – возвращает список, состоящий из count случайных паролей длиной length
символов.
Примечание 3. Приведенные ниже тесты – это лишь образцы возможного ответа. Возможны и другие способы генерации паролей.
"""
import random
import string


def generate_password(length):
    abc_upper = {i for i in string.ascii_uppercase} - set('lI1oO0')
    abc_lower = {i for i in string.ascii_lowercase} - set('lI1oO0')
    digits = {i for i in string.digits} - set('lI1oO0')

    password = list(''.join(random.sample(list(abc_upper | abc_lower | digits), length - 3)) + \
                    ''.join(random.choice(list(abc_upper))) + ''.join(random.choice(list(abc_lower))) + \
                    ''.join(random.choice(list(digits))))
    random.shuffle(password)
    return ''.join(password)


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


n, m = int(input()), int(input())

print(*generate_passwords(n, m), sep='\n')

