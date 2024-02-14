"""Предикат делимости"""

n1 = int(input())
n2 = int(input())


def func(num1, num2):
    if num1 % num2 == 0:
        return 'делится'
    else:
        return 'не делится'

print(func(n1, n2))
