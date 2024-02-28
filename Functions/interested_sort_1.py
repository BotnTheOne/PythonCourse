n = input().split()
lst_n = list(n)


def interest_sort(arg):
    res = [int(i) for i in str(arg)]
    return sum(res)


new_lst = sorted(lst_n, key=interest_sort)
print(*new_lst)
