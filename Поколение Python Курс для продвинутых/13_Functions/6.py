"""
Следующий программный код:

print_products([4], {}, 1, 2, {'Beegeek'}, '')
должен выводить:

Нет продуктов
Примечание 4. Обратите внимание: функция print_products() должна выводить (печатать) нужное значение, а не возвращать
его.

Примечание 5. Вызывать функцию print_products() не нужно, требуется только реализовать.
"""


def print_products(*args):
    products = []
    num = 1
    for item in args:
        if type(item) is str and item != '':
            products.append(str(num) + ') ' + item)
            num += 1
    print(*(['Нет продуктов'], products)[len(products) != 0], sep='\n')


def best_print_products(*args):
    cnt = 0
    for e in args:
        if type(e) == str and e:
            cnt += 1
            print(f'{cnt}) {e}')
    if cnt == 0:
        print('Нет продуктов')


print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')