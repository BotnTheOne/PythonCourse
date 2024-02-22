s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

lst_s = s.split()
result = {}
result_new = {}


for i in lst_s:
    result[i] = result.get(i, 0) + 1

max_num = max(result.values())

for key, value in result.items():
    if value == max_num:
        result_new[key] = result_new.get(key, value)
max_num2 = (min(result_new))

print(max_num2)
