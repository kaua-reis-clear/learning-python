# person = {
#     'first_name': 'Kauã',
#     'last_name': 'Drar',
#     'age': 18,
#     'height': 1.8,
#     'addresses': [
#         {'street': 'foo foo', 'number': 123},
#         {'street': 'bar bar', 'number': 321},
#     ]
# }
# person = dict(first_name='Kauã', last_name='Drar')
person = {
    'first_name': 'Kauã',
    'last_name': 'Drar',
    'age': 18,
    'height': 1.8,
    'addresses': [
        {'street': 'foo foo', 'number': 123},
        {'street': 'bar bar', 'number': 321},
    ],
}
# print(person, type(person))
print(person['first_name'])
print(person['last_name'])

print()

for key in person:
    print(key, person[key])