"""Орел и решка"""

n = input()
max_n = 0
p_list = n.split('О')

for i in p_list:
    x = len(i)
    if x > max_n:
        max_n = x
print(max_n)
