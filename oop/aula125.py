class Person:
    current_year = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.current_year = 100

    def get_birth_year(self):
        return Person.current_year - self.age
    
p1 = Person('Kauã', 18)
p2 = Person('Cintia', 45)

print(Person.current_year)
# Person.current_year = 1

print(p1.get_birth_year())
print(p2.get_birth_year())