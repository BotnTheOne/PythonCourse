def info_kwargs(**kwargs):
    my_dct = {}
    my_dct.update(kwargs)
    sorted_dct = dict(sorted(my_dct.items()))

    for key, value in sorted_dct.items():
        print(f'{key}: {value}')

info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
