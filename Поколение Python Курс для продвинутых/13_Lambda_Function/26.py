"""
Напишите программу, которая с помощью встроенных функций filter() и sorted() выводит слова из списка words, имеющие
длину ровно
6
6 символов. Слова следует вывести в алфавитном порядке на одной строке, разделив символом пробела.
"""
words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able',
         'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound',
         'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday',
         'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry',
         'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
print(*sorted(filter(lambda s: len(s) == 6, words)))