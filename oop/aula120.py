# string = 'Kauã'  # str
# print(string.upper())
# print(isinstance(string, str))
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


p1 = Person('Kauã', 'Drar')
# p1.first_name = 'Kauã'
# p1.last_name = 'Drar'

p2 = Person('Vitória', 'Rossi')
# p2.first_name = 'Vitória'
# p2.last_name = 'Rossi'

print(p1.first_name)
print(p1.last_name)

print(p2.first_name)
print(p2.last_name)