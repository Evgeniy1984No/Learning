"""
Для матрицы

А =   1 0
      4 1
Найти А^25
"""

a = [[int(i) for i in input().split()], [int(i) for i in input().split()]]
[print(*[str(j) for j in i]) for i in a]
b = []
[b.append(i) for i in a]
print()
[print(*[str(j) for j in i]) for i in b]
elem = 0
c = [[0] * 2 for _ in range(2)]

for k in range(24):
    for ci in range(2):
        for cj in range(2):
            for j in range(2):
                c[ci][cj] += a[ci][j] * b[j][cj]

    a = c
    c = [[0] * 2 for _ in range(2)]

[print(*[str(j) for j in i]) for i in a]