"""Зеркальное отображение"""

n = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(n)]

for i in range(int(len(matrix) / 2)):
    matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]

for j in matrix:
    print(*j)
# print(matrix)
