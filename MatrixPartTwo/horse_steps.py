"""Ходы коня"""

t, r = input(), range(8)
y, x = ord(t[0]) - ord("a"), int(t[1]) - 1
t = [[".*"[((x - i) ** 2 - (y - j) ** 2) ** 2 == 9] for j in r] for i in r]
t[x][y] = "N"

[print(*x) for x in t[::-1]]
