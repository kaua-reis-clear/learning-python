import json

FILE_PATH = 'aula127.json'


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Kauã', 33)
p2 = Person('Vitória', 21)
p3 = Person('Cintia', 11)
bd = [vars(p1), p2.__dict__, vars(p3)]


def dump():
    with open(FILE_PATH, 'w') as file:
        print('DUMPING')
        json.dump(bd, file, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    print('HE IS THE __main__')
    dump()