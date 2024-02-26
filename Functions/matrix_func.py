def matrix(n=1, m=None, value=0):
    if m is None:
        return [[value for num in range(n)] for i in range(n)]
    else:
        return [[value for num in range(m)] for i in range(n)]

print(matrix())
print(matrix(3))
print(matrix(2, 5))
print(matrix(3, 4, 9))
