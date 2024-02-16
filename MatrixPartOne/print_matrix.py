"""Вывести матрицу 1"""

rows = int(input())
cols = int(input())

matrix = [[input() for _ in range(cols)] for _ in range(rows)]

for i in matrix:
    res = ' '.join(i)
    print(res)
