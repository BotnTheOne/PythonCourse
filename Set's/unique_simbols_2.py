"""Уникальные символы 2"""

n = int(input())

res_word = ''

for i in range(n):
    word = input().lower()
    res_word += word

unique_simbols = set(res_word)
print(len(unique_simbols))
