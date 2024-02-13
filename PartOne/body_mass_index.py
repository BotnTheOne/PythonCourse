"""Индекс массы тела"""

mass = float(input())
height = float(input())

body_mass_index = mass / (height ** 2)

if body_mass_index < 18.5:
    print("Недостаточная масса")
elif body_mass_index > 25:
    print("Избыточная масса")
else:
    print("Оптимальная масса")
