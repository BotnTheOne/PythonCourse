
is_num = lambda x: True if '-' not in x[1:] and x.replace('.', '', 1).replace('-', '', 1).isdigit() and x.count('.') < 2 else False

print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))
