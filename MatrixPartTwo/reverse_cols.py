"""Обмен столбцов"""

n = int(input())
m = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(n)]

i, j = map(int, input().split())

for o in matrix:
    o[i], o[j] = o[j], o[i]

for _ in matrix:
    print(*_)
