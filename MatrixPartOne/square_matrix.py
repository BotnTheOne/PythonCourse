"""След матрицы"""

n = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(n)]
summ = 0

for i in range(n):
    for j in range(n):
        if i == j:
            summ += matrix[i][j]

print(summ)
