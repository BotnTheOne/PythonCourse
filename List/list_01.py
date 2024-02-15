"""Список по образцу 1"""

n = int(input())
my_list = []

for i in range(n):
    res = [int(j + 1) for j in range(n)]
    my_list.append(res)

for row in my_list:
    print(row)
