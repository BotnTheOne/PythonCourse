"""Общие цифры"""

n = int(input())
lst_nums = []


for i in range(n):
    num = int(input())
    lst_nums.append(set(str(num)))

set_nums = set.intersection(*lst_nums)

# print(lst_nums)
print(*sorted(set_nums))
