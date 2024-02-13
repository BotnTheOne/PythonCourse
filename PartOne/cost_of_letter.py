"""Стоимость строки"""

letter = str(input())
# letter = "Привет, как дела!?"
symbol_cost = 60

cost_of_letter = len(letter) * symbol_cost
cost_in_rub = int(cost_of_letter // 100)
# cost_in_cop = (round(float(cost_of_letter % 1), 2)) * 100
cost_in_cop = (cost_of_letter % 100)

# print(cost_of_letter)
# print(cost_in_rub)
# print(cost_in_cop)
print(f"{cost_in_rub} р. {cost_in_cop} коп.")
