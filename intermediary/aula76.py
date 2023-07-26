person = {}

##
##

chave = 'first_name'

person[chave] = 'Kauã'
person['first_name'] = 'Drar'


print(person[chave])

person[chave] = 'Cintia'

del person['first_name']
print(person)
print(person['first_name'])

# print(person.get('first_name'))
if person.get('first_name') is None:
    print("DOESN'T EXIST")
else:
    print(person['first_name'])