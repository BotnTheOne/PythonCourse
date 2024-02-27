def print_products(*args):
    products = []
    for i in args:
        if type(i) == str and i != '':
            products.append(i)

    for j in range(len(products)):
        if len(products) >= 1:
            print(f'{j+1}) {products[j]}')
        # elif len(products) == 0:
        #     print("Нет продуктов")

    if len(products) == 0:
        print("Нет продуктов")
print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')