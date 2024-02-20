"""Встречалось ли число раньше?"""

num_set = set()
num_lst = [int(i) for i in input().split()]

for j in num_lst:
    if j not in num_set:
        num_set.add(j)
        print('NO')
    else:
        print('YES')
