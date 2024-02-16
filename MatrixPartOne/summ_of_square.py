"""Сумма четвертей"""

n = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(n)]
res_list_left = []
res_list_right = []
res_list_up = []
res_list_down = []

for i in range(n):
    for j in range(n):
        if i > j and i < (n - 1 - j):
            res_list_left.append(matrix[i][j])
        elif i < j and i > (n - 1 - j):
            res_list_right.append(matrix[i][j])
        elif i < j and i < (n - 1 - j):
            res_list_up.append(matrix[i][j])
        elif i > j and i > (n - 1 - j):
            res_list_down.append(matrix[i][j])

print(f"Верхняя четверть: {sum(res_list_up)}")
print(f"Правая четверть: {sum(res_list_right)}")
print(f"Нижняя четверть: {sum(res_list_down)}")
print(f"Левая четверть: {sum(res_list_left)}")

