"""
Итератор Alphabet 🌶️
Реализуйте класс Alphabet, порождающий итераторы, конструктор которого принимает один аргумент:

language — код языка: ru — русский, en — английский
Итератор класса Alphabet() должен циклично генерировать последовательность строчных букв:

русского алфавита, если language имеет значение ru
английского алфавита, если language имеет значение en
Примечание 1. Буква ё в русском алфавите не учитывается.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс Alphabet.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

ru_alpha = Alphabet('ru')

print(next(ru_alpha))
print(next(ru_alpha))
print(next(ru_alpha))
Sample Output 1:

а
б
в
Sample Input 2:

en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)
Sample Output 2:

a b c d e f g h i j k l m n o p q r s t u v w x y z a b
"""


class MyAlphabet:
    def __init__(self, language):
        if language == 'ru':
            self.span = [chr(i) for i in range(1072, 1104)]
        else:
            self.span = [chr(i) for i in range(97, 123)]
        self.alpha = iter(self.span)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.alpha)
        except StopIteration:
            self.alpha = iter(self.span)
            return next(self.alpha)


# ******************************************************************************************************************

class Alphabet:
    def __init__(self, language: str):
        if language == "ru":
            self.alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        elif language == "en":
            self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        self.index %= len(self.alphabet)
        return self.alphabet[self.index]


en_alpha = MyAlphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)

