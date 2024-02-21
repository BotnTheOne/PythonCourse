"""Количество совпадающих"""

n = input().split()
m = input().split()

set_n = set(n)
set_m = set(m)
set_res = set_n.intersection(set_m)

print(len(set_res))

