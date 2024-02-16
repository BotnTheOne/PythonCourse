"""Таблица умножения"""

n = int(input())
m = int(input())

matrix = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = i * j

for rows in matrix:
    for cols in rows:
        print(str(cols).ljust(3), end=' ')
    print()
