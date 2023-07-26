# Métodos úteis dos dicionários em Python
# len - how many keys
# keys - iterable with dict keys
# values - iterable with dict values
# items - iterable with keys and values
# setdefault - set value if key doesn't exists
# copy - returns a shallow copy
# get - gets a key
# pop - delete an item with the specified key
# popitem - delete the last added key
# update - updates a dict with another one
p1 = {
    'first_name': 'Kauã',
    'last_name': 'Drar',
}

# p1.update({
#     'first_name1': 'AAAA',
#     'last_name1': 'BBBB',
#     'age': 123,
# })
# p1.update(age=123, first_name='Qualquer outro')
variable = (1,)
print(variable)
p1.update(
    (
        ('Key', 'Value'),
        ('Key1', 'Value1'),
        ('Key2', 'Value1'),
    )
)
print(p1)
# print(p1.get('first_name', 'Default value'))

# first_name = p1.pop('first_name')
# print(first_name)
# print(p1)

# last_key = p1.popitem()
# print(last_key)
# last_key = p1.popitem()
# print(last_key)
# print(p1)