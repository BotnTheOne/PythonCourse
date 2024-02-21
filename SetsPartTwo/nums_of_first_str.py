"""Числа первой строки"""

n = input().split()
m = input().split()

set_n = set(n)
set_m = set(m)
set_res = set_n.difference(set_m)
lst_res = []

for i in set_res:
    lst_res.append(int(i))
lst_sort = sorted(lst_res)

print(*lst_sort)
