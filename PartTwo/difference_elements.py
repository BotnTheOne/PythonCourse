"""Различные элементы"""

n = input().split()
num_list = []

for i in n:
    num_list.append(int(i))

num_list = set(num_list)
res = len(num_list)
print(res)
