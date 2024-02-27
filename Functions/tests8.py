points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]


def sort_points(n):
    res_lst = []
    for i in n:
        res = (i[0]**2 + i[1]**2)**0.5
        res_lst.append(res)
    points_dct = dict(zip(res_lst, points))
    sorted_dct = dict(sorted(points_dct.items()))
    res_values = list(sorted_dct.values())
    return res_values

points = sort_points(points)
print(points)
