"""Сдвиг в развитии"""

n = input().split()
num_list = []

for i in n:
    num_list.append(int(i))

x = num_list[len(num_list) - 1]
num_list.pop(len(num_list) - 1)
num_list.insert(0, x)

for i in num_list:
    print(i, end=' ')
