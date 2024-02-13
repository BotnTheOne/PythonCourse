"""Перевод числа"""

number = str(input())

if len(number) == 5:
    reverse_number = number[::-1]
else:
    reverse_number = number[0:1] + number[-1:-6:-1]
int_number = int(reverse_number)
print(int_number)
