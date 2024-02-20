"""Все 10 цифр"""

n = input()
m = input()

set_n = set(n)
set_m = set(m)
sum_sets = set_n.union(set_m)
set_of_ten_nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

if sum_sets == set_of_ten_nums:
    print('YES')
else:
    print('NO')
