"""Список по образцу 2"""

n = int(input())
my_list = []

for i in range(n):
    res = [i + 1 for i in range(i + 1)]
    my_list.append(res)

for row in my_list:
    print(row)
