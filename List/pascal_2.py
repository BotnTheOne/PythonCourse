"""Треугольник Паскаля 2"""

n = int(input())
s = []
for i in range(n):
    row = [1]*(i+1)
    for j in range(i+1):
        if j != i and j != 0:
            row[j] = s[i-1][j-1] + s[i-1][j]
    s.append(row)

for j in s:
    print(*j)
