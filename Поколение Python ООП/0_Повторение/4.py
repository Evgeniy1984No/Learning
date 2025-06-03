"""
Функция intersperse()
Реализуйте генераторную функцию intersperse(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
delimiter — значение-разделитель
Функция должна возвращать генератор, порождающий последовательность из элементов итерируемого объекта iterable, между
которыми располагается значение-разделитель delimiter.

Примечание 1. Рассмотрим первый тест, в котором в качестве итерируемого объекта передается список чисел от 1 до 3, а в
качестве значения-разделителя — 0. Порождаемая генератором последовательность состоит из чисел 1, 2 и 3, между которыми
располагается число 0:

1 0 2 0 3
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию intersperse(), но не код,
вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(*intersperse([1, 2, 3], 0))
Sample Output 1:

1 0 2 0 3
Sample Input 2:

inter = intersperse('beegeek', '!')
print(next(inter))
print(next(inter))
print(*inter)
Sample Output 2:

b
!
e ! e ! g ! e ! e ! k
Sample Input 3:

print(*intersperse('A', '...'))
Sample Output 3:

A
"""


def intersperse(iterb, delm):
    res = []
    for i in iterb:
        res.append(i)
        res.append(delm)
    for j in res[:-1]:
        yield j


inter = intersperse('beegeek', '---')
print(*inter)
print('---'.join('beegeek'))
# print(next(inter))
# print(next(inter))
# print(*inter)

