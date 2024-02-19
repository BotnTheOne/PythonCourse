"""Последовательность Трибоначчи"""

n = int(input())
num1, num2, num3 = 1, 1, 1

for i in range(n):
    print(num1, end=' ')
    num1, num2, num3 = num2, num3, num1 + num2 + num3
