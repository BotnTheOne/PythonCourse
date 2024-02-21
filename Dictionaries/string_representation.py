"""Строковое представление"""

n = int(input())
num_dict = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
res_lst = []

for i in str(n):
    res_lst.append(num_dict[i])

print(*res_lst)
