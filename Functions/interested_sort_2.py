n = sorted([int(i) for i in input().split()])


def interest_sort(arg):
    res = [int(i) for i in str(arg)]
    return sum(res)


new_lst = sorted(n, key=interest_sort)
print(*new_lst)
