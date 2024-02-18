"""Максимум в таблице"""

n = int(input())
m = int(input())
# n = 6
# m = 8
max_num_lst = []
indx_max = []
max_num = 0

matrix = [[int(i) for i in input().split()] for _ in range(n)]
# matrix = [[-4, -3, -4, -4, -1, -8, -2, -3],
#           [-2, -3, -9, -7, -3, -4, -4, -5],
#           [-4, -3, -4, -4, -1, -2, -2, -3],
#           [-2, -3, -9, -3, -3, -1, -4, -5],
#           [-5, -3, -4, -4, -1, -2, -2, -3],
#           [-2, -3, -7, -8, -3, -4, -4, -5]]

for i in matrix:
    for j in i:
        max_num_lst.append(max(i))
max_num=max(max_num_lst)

for l in range(n):
    for k in range(m):
        if max_num == matrix[l][k]:
            indx_max.append([l, k])

# print(indx_max)
a, b = indx_max[0]
print(a, b)
