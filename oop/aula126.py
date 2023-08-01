class Person:
    current_year = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.current_year = 100

    def get_birth_year(self):
        return Person.current_year - self.age
    


data = {'name': 'Kauã', 'age': 20}
p1 = Person(**data)
# p1.nome = 'FOO'
# print(p1.age)
# p1.__dict__['some'] = 'thing'
# p1.__dict__['name'] = 'FOO'
# del p1.__dict__['some']
# print(p1.__dict__)
# print(vars(p1))
# print(p1.some)
# print(p1.nome)
print(vars(p1))