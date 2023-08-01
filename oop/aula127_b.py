import json

from aula127_a import FILE_PATH, Person, dump

# dump()

with open(FILE_PATH, 'r') as file:
    people = json.load(file)
    p1 = Person(**people[0])
    p2 = Person(**people[1])
    p3 = Person(**people[2])

    print(p1.name, p1.age)
    print(p2.name, p2.age)
    print(p3.name, p3.age)