"""
Итератор CardDeck
Реализуйте класс CardDeck, порождающий итераторы, конструктор которого не принимает никаких аргументов.

Итератор класса CardDeck должен генерировать последовательность из
52
52 игральных карт, а после возбуждать исключение StopIteration. Каждая карта должна представлять собой строку в
следующем формате:

<номинал> <масть>
Например, 7 пик, валет треф, дама бубен, король червей, туз пик.

Примечание 1. Карты, генерируемые итератором, должны располагаться сначала по величине номинала, затем масти.

Примечание 2. Старшинство мастей по возрастанию: пики, трефы, бубны, червы. Старшинство карт в масти по возрастанию:
двойка, тройка, четверка, пятерка, шестерка, семерка, восьмерка, девятка, десятка, валет, дама, король, туз.

Примечание 3. Масти не требуют склонения и независимо от номинала должны сохранять следующее написание: пик, треф,
бубен, червей.

Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимый класс CardDeck.

Примечание 5. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

cards = CardDeck()

print(next(cards))
print(next(cards))
Sample Output 1:

2 пик
3 пик
Sample Input 2:

cards = list(CardDeck())

print(cards[9])
print(cards[23])
print(cards[37])
print(cards[51])
Sample Output 2:

валет пик
дама треф
король бубен
туз червей
"""


class MyCardDeck:
    def __init__(self):
        self.nominals = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")
        self.suits = iter(["пик", "треф", "бубен", "червей"])
        self.index_n = -1
        self.suit = next(self.suits)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.index_n += 1
            return f'{self.nominals[self.index_n]} {self.suit}'
        except IndexError:
            self.index_n = 0
            try:
                self.suit = next(self.suits)
                return f'{self.nominals[self.index_n]} {self.suit}'
            except:
                raise StopIteration


# *******************************************************************************************************************

class CardDeck:
    def __init__(self):
        suit = ('пик', 'треф', 'бубен', 'червей')
        number = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз')
        self.deck = iter(f'{j} {i}' for i in suit for j in number)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.deck)


cards = list(CardDeck())

print(cards[9])
print(cards[23])
print(cards[37])
print(cards[51])
