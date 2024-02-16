"""Максимальный в области 2"""

n = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(n)]
res_list = []

for i in range(n):
    for j in range(n):
        if i >= j and i <= (n - 1 - j) or i <= j and i >= (n - 1 - j):
            res_list.append(matrix[i][j])
print(max(res_list))
