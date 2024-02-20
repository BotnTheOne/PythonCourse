"""Уникальные символы 1"""

n = int(input())
word_lst = []

for i in range(n):
    word = set(input().lower())
    word_lst.append(len(word))

for j in word_lst:
    print(j, sep='\n')
