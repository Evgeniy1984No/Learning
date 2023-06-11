dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}
for i in dict1:
    result[i] = result.get(i, dict1.get(i))
for j in dict2:
    if j in result:
        result[j] = result.get(j, dict2.get(j)) + dict2.get(j)
    else:
        result[j] = result.get(j, dict2.get(j))

"""
_____________________________________________________________________________________
"""
result = dict1.copy()
for key, value in dict2.items():
    result[key] = result.get(key, 0) + value


def f(n=3):
    return n + 7


print(f(f(f())))