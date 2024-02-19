"""Конкурсный отбор"""

n = int(input())
students_lst = []

for i in range(n):
    name = input().split()
    students_lst.append(name)
    n -= 1

for _ in students_lst:
    print(*_)
print()

for j in students_lst:
    if j[-1] >= '4':
        print(*j)

# print(students_lst)
