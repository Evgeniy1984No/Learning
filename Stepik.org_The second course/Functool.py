from functools import partial

x = int("1101101", base=2)
print(x)
int_2 = partial(int, base=2)
x = int_2("1101101")
print(x)


names = [
    ('Guido', 'van', 'Rossum'),
    ('Haskell', 'Curry'),
    ('John', 'Backus')
]

import operator as op

names.sort(key=op.itemgetter(0))
# print(names)

sort_by_last = partial(list.sort, key=op.itemgetter(-1))
print(names)
sort_by_last(names)
print(names)
