from math import sin

n = int(input())
word = input()


def square(num):
    return num**2


def cube(num):
    return num ** 3


def square_root(num):
    return num ** 0.5


def module(num):
    return abs(num)


def sinus(num):
    return sin(num)


func_dct = {
    'квадрат': square,
    'куб': cube,
    'корень': square_root,
    'модуль': module,
    'синус': sinus,
}

res = func_dct[word](n)
print(res)
