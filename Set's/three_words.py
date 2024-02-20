"""Три слова"""

word = input()

word_lst = word.split(' ')

if set(word_lst[0]) == set(word_lst[1]) == set(word_lst[2]):
    print('YES')
else:
    print('NO')
