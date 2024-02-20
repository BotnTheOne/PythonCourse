"""Неповторимые цифры"""

n = int(input())
n = str(n)

set_n = set(n)

if len(set_n) == len(n):
    print('YES')
else:
    print('NO')
