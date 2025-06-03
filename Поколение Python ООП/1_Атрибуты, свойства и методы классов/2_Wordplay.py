"""
Класс Wordplay
Будем называть словом любую последовательность из одной или более латинских букв.

Реализуйте класс Wordplay, описывающий расширяемый набор слов. При создании экземпляра класс должен принимать один
аргумент:

words — список, определяющий начальный набор слов. Если не передан, начальный набор слов считается пустым
Экземпляр класса Wordplay должен иметь один атрибут:

words — список, содержащий набор слов
Класс Wordplay должен иметь четыре метода экземпляра:

add_word() — метод, принимающий в качестве аргумента слово и добавляющий его в набор. Если слово уже есть в наборе,
метод ничего не должен делать
words_with_length() — метод, принимающий в качестве аргумента натуральное число n и возвращающий список слов из набора,
длина которых равна n
only() — метод, принимающий произвольное количество аргументов — букв, и возвращающий все слова из набора, которые
включают в себя только переданные буквы
avoid() — метод, принимающий произвольное количество аргументов — букв, и возвращающий все слова из списка words,
которые не содержат ни одну из этих букв
Примечание 1. Слова в списках, возвращаемых методами words_with_length(), only() и avoid(), должны располагаться в том
порядке, в котором они были добавлены.

Примечание 2. Экземпляр класса Wordplay не должен зависеть от списка, на основе которого он был создан. Другими словами,
если исходный список изменится, то экземпляр класса Wordplay измениться не должен.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

wordplay = Wordplay()

print(wordplay.words_with_length(1))
print(wordplay.only('a', 'b', 'c'))
print(wordplay.avoid('a', 'b', 'c'))
Sample Output 1:

[]
[]
[]
Sample Input 2:

wordplay = Wordplay()

print(wordplay.words)
wordplay.add_word('bee')
wordplay.add_word('geek')
print(wordplay.words)
Sample Output 2:

[]
['bee', 'geek']
Sample Input 3:

wordplay = Wordplay(['bee', 'geek', 'cool', 'stepik'])

wordplay.add_word('python')
print(wordplay.words_with_length(4))
Sample Output 3:

['geek', 'cool']
Sample Input 4:

wordplay = Wordplay(['o', 'to', 'otto', 'top', 't'])

print(wordplay.only('o', 't'))
Sample Output 4:

['o', 'to', 'otto', 't']
"""
import re


class Wordplay:
    def __init__(self, words: list = None):
        if words is None:
            self.words = []
        else:
            self.words = words.copy()

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        return [w for w in self.words if len(w) == n]

    def only(self, *args):
        pattern = fr'[{args}]+'
        return [w for w in self.words if re.fullmatch(pattern, w)]

    def avoid(self, *args):
        pattern = fr'[{args}]+'
        return [w for w in self.words if not re.search(pattern, w)]
