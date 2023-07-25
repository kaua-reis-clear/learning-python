def greeting(msg, nome):
    return f'{msg}, {nome}!'


def execute(my_function, *args):
    return my_function(*args)


print(
    execute(greeting, 'Good morning', 'Kauã')
)
print(
    execute(greeting, 'Good night', 'Vitória')
)