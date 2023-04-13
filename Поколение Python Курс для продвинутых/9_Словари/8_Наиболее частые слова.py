"""
Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s. Если таких слов несколько,
должно быть выведено то, что меньше в лексикографическом порядке.
"""
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange ' \
    'barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry ' \
    'apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana ' \
    'melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry ' \
    'gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley ' \
    'plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley ' \
    'lime grapefruit pomegranate barley'
result = {}

for word in s.split():
    result[word] = result.get(word, 0) + 1

print(result)
name, num = result.popitem()
print(name, num)
for key, value in result.items():
    if value > num:
        name, num = key, value
    elif value == num:
        if key < name:
            name, num = key, value
print(name, num)
"""
____________________________________________________________________________________
лямбда задает ключ по которому будут сравниваться элементы при выборе наиболее часто встречающегося элемента. 
У нас есть два критерия. Один требует выбрать слово с наибольшей частотой повторорений, второй - выбрать из таких 
повторяющихся слов наименьшее в лексикографическом порядке. Когда есть несколько критериев обычно их перечисляют в виде 
кортежа (или списка), потому что два кортежа (списка) сравниваются между собой именно так: сначала сравниваются первые 
элементы кортежа и только если они совпадают - сравниваются вторые и т.д. Вот мы и формируем кортеж состоящий из частоты 
повтороений слова и самого слова. Но в данном случае получаетя противоречие между двумя критериями выбора. Один ищет 
максималное значение, другой - минимальное в лексикографическом порядке, а мы умеем искать либо минимальное либо 
максимальное. Эту дилемму можно решить, взяв значения частоты повторений с минусом, тогда наибольшие значения частоты 
повторений станут наименьшими и наоборот! Теперь оба критерия подходять для выбора минимального значения.
"""
d = {}
for w in s.split():
    d[w] = d.get(w, 0) + 1
print(min(d, key=lambda x: (-d[x], x)))