"""Произведение чисел"""

n = int(input())
num_list = []
count = 0
while n > 0:
    num = int(input())
    num_list.append(num)
    n -= 1

multi = int(input())

if len(num_list) > 3:
    for i in range(len(num_list) - 1):
        for j in range(i, len(num_list) - 1):
            if num_list[i] * num_list[j] == multi:
                count += 1
            else:
                pass
else:
    for k in range(len(num_list) - 1):
        if num_list[k] * num_list[k + 1] == multi:
            count += 1

if count > 0:
    print('ДА')
else:
    print('НЕТ')
# print(num_list)
# print(multi)
