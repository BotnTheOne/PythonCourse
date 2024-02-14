"""Больше предыдущего"""

n = input().split()
num_list = []
count = 0

for i in n:
    num_list.append(int(i))

for j in range(len(num_list) - 1):
    if num_list[j] < num_list[j + 1]:
        count += 1

print(count)
