"""Количество слов в тексте"""
import re

n = input().lower()
n = re.findall('[a-zа-яё]+', n, flags=re.IGNORECASE)

word = set(n)

print(len(word))

