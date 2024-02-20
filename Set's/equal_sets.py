"""Одинаковые наборы"""

n = input()
m = input()

set_n = set(n)
set_m = set(m)

if set_n == set_m:
    print('YES')
else:
    print('NO')
