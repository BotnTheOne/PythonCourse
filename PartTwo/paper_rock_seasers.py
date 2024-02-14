"""Камень, ножницы, бумага"""

timur = input()
ruslan = input()

if timur == 'камень' and ruslan == 'бумага' or timur == 'ножницы' and ruslan == 'камень' or timur == 'бумага' and ruslan == 'ножницы':
    print('Руслан')
elif timur == ruslan:
    print('ничья')
else:
    print('Тимур')
