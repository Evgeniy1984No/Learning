"""
Класс CaseHelper 🌶️🌶️
Snake Case — стиль написания составных слов, при котором несколько слов разделяются символом нижнего подчеркивания (_)
и не имеют пробелов в записи, причём каждое слово пишется с маленькой буквы. Например, bee_geek и hello_world.

Upper Camel Case — стиль написания составных слов, при котором несколько слов пишутся слитно без пробелов, при этом
каждое слово пишется с заглавной буквы. Например, BeeGeek и HelloWorld.

Реализуйте класс CaseHelper, описывающий набор функций для работы со строками в стилях Snake Case и Upper Camel Case.
 При создании экземпляра класс не должен принимать никаких аргументов.

Класс CaseHelper должен иметь четыре статических метода:

is_snake() — метод, принимающий в качестве аргумента строку и возвращающий True, если переданная строка записана в
стиле Snake Case, или False в противном случае
is_upper_camel() — метод, принимающий в качестве аргумента строку и возвращающий True, если переданная строка записана
в стиле Upper Camel Case, или False в противном случае
to_snake() — метод, который принимает в качестве аргумента строку в стиле Upper Camel Case, записывает ее в стиле Snake
Case и возвращает полученный результат
to_upper_camel() — метод, который принимает в качестве аргумента строку в стиле Snake Case, записывает ее в стиле
Upper Camel Case и возвращает полученный результат
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(CaseHelper.is_snake('beegeek'))
print(CaseHelper.is_snake('bee_geek'))
print(CaseHelper.is_snake('Beegeek'))
print(CaseHelper.is_snake('BeeGeek'))
Sample Output 1:

True
True
False
False
Sample Input 2:

print(CaseHelper.is_upper_camel('beegeek'))
print(CaseHelper.is_upper_camel('bee_geek'))
print(CaseHelper.is_upper_camel('Beegeek'))
print(CaseHelper.is_upper_camel('BeeGeek'))
Sample Output 2:

False
False
True
True
Sample Input 3:

print(CaseHelper.to_snake('Beegeek'))
print(CaseHelper.to_snake('BeeGeek'))
Sample Output 3:

beegeek
bee_geek
Sample Input 4:

print(CaseHelper.to_upper_camel('beegeek'))
print(CaseHelper.to_upper_camel('bee_geek'))
Sample Output 4:

Beegeek
BeeGeek
"""
import re


class CaseHelper:
    __snake_pattern = r'[a-z]+(_[a-z]+)*[a-z]+'
    __camel_pattern = r'([A-Z][a-z]+)+'
    __to_snake = r'[A-Z][a-z]+'

    @staticmethod
    def is_snake(s):
        return bool(re.fullmatch(CaseHelper.__snake_pattern, s))

    @staticmethod
    def is_upper_camel(s):
        return bool(re.fullmatch(CaseHelper.__camel_pattern, s))

    @staticmethod
    def to_snake(s):
        return '_'.join(map(str.lower, re.findall(CaseHelper.__to_snake, s)))

    @staticmethod
    def to_upper_camel(s):
        return ''.join(map(str.capitalize, re.findall(r'[a-z]+', s)))