"""Симметричная матрица"""

n = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(n)]
left_matrix = []
right_matrix = []


if len(matrix) == 2:
    if matrix[0][1] == matrix[1][0]:
        print('YES')
    else:
        print('NO')
elif len(matrix) > 3:
    for i in range(n):
        for j in range(n):
            if i > j and (i < n - 1 - j) or i > j and (i > n - 1 - j):
                left_matrix.append(matrix[i][j])
            elif i < j and (i < n - 1 - j) or i < j and (i > n - 1 - j):
                right_matrix.append((matrix[i][j]))
    left_matrix.sort()
    right_matrix.sort()
    if left_matrix == right_matrix:
        print('YES')
    else:
        print('NO')
else:
    if matrix[0][1] == matrix[1][0] and matrix[1][2] == matrix[2][1]:
        print('YES')
    else:
        print('NO')

# print(left_matrix)
# print(right_matrix)

