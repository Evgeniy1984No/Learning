desk = [['.'] * 8 for _ in range(8)]
col_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
print(desk)
[print(*row) for row in desk]
print()
n = input()
i = ~int(n[1])+1
j = col_dict[n[0]]
desk[i][j] = 'N'
[print(*row) for row in desk]
print(i)
print(i+11 in range(8))