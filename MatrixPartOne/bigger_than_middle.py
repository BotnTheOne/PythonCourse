"""Больше среднего"""

n = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(n)]


for i in matrix:
    middle = sum(i) / len(i)
    count = 0
    for j in i:
        if j > middle:
            count += 1
    print(count)
