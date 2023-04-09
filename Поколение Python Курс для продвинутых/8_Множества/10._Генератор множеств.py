"""
Используя генератор множеств, дополните приведенный код так, чтобы получить множество, содержащее уникальные значения списка items. Результат вывести на одной строке, в упорядоченном виде, разделяя элементы одним символом пробела.

Примечание 1. Обратите внимание, некоторые элементы списка – числа, а некоторые – строки, при этом строки необходимо трактовать как числа.

Примечание 2. Чтобы вывести элементы множества в упорядоченном виде используйте следующий код:

print(*sorted(myset))
"""
items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
s_items = {int(i) for i in items}
# print(*sorted(s_items))
words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon',
         'tangerine', 'Watermelon', 'currant', 'Almond']
s_words = {w[0].lower() for w in words}
# print(*sorted(s_words))
sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a 
pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if 
you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those 
redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the 
rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
s_sentence = {word.strip(':,.!?();').lower() for word in sentence.split()}
print(*sorted(s_sentence))