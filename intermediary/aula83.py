a, b = 1, 2
a, b = b, a
# print(a, b)


# (a1, a2), (b1, b2) = person.items()
# print(a1, a2)
# print(b1, b2)

# for key, value in person.items():
#     print(key, value)

person = {
    'first_name': 'Kauã',
    'last_name': 'Drar',
}

person_infos = {
    'age': 16,
    'height': 1.6,
}

person_complete = {**person, **person_infos}
print(person_complete)

# kwargs - keyword arguments

def show_keyword_arguments(*args, **kwargs):
    print('NOT A KEYWORD:', args)

    for key, value in kwargs.items():
        print(key, value)


# show_keyword_arguments(first_name='Cintia', qlq=123)
# show_keyword_arguments(**person_complete)

configs = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
show_keyword_arguments(**configs)