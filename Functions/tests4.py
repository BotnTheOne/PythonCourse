def greet(name, *args):
    a = 'Hello,'
    name = name.split()
    args = list(args)
    name.extend(args)
    name = ' and '.join(name)
    return a + ' ' + name + '!'


print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))
