"""Координаты четверти"""

n = int(input())
point_list = []
count_one = 0
count_two = 0
count_three = 0
count_four = 0
# n = 10

while n > 0:
    x, y = input().split()
    point_list.append([int(x), int(y)])
    n -= 1

for i in point_list:
    if i[0] > 0 and i[1] > 0:
        count_one += 1
    elif i[0] < 0 and i[1] > 0:
        count_two += 1
    elif i[0] < 0 and i[1] < 0:
        count_three += 1
    elif i[0] > 0 and i[1] < 0:
        count_four += 1
    else:
        pass

# print(point_list)
# print(count_one, count_two, count_three, count_four)
#
print(f"Первая четверть: {count_one} \nВторая четверть: {count_two} \nТретья четверть: {count_three} \nЧетвертая четверть: {count_four}\n")
