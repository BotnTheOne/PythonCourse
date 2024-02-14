"""Вперед, назад и наоборот"""

n = input().split()
num_list = []

for i in n:
    num_list.append(int(i))

for j in range(0, len(num_list) - 1, 2):
    num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

for k in num_list:
    print(k, end=' ')
