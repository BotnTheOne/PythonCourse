"""Вершина параболы"""

a = int(input())
b = int(input())
c = int(input())

x = - (b / (2 * a))
y = ((4 * a * c) - (b ** 2)) / 4 / a

res = (x, y)
print(res)
