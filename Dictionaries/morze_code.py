"""Код Морзе"""

letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

morse_dct = dict(zip(letters, morse))

word = ''.join(i for i in input().upper() if i.isalnum())
res_lst = []

for i in word:
    res_lst.append(morse_dct[i])

print(*res_lst, sep=' ')
