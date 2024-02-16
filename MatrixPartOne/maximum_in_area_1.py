"""Максимальный в области 1"""

n = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(n)]
res_list = []

for i in range(n):
    for j in range(n):
        if i >= j:
            res_list.append(matrix[i][j])
print(max(res_list))
