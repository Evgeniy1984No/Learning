def same_lambda(any_var):
    return any_var % 2 == 0


# values = (int(i) for i in input().split())
# print(values)
# evens = list(filter(lambda any_var: any_var % 2 == 0, values))
# # evens = list(filter(same_lambda, values))
# print(evens)

names = [
    ('Guido', 'van', 'Rossum'),
    ('Haskell', 'Curry'),
    ('John', 'Backus')
]


def length(name):
    return len(" ".join(name))


name_lengths = [length(name) for name in names]
print(name_lengths)

# names.sort(key=length)
# print(names)

names.sort(key=lambda name: len(" ".join(name)))
print(names)

import operator as op

names.sort(key=op.itemgetter(0))
print(names)
