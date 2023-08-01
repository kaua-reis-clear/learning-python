class Car:
    def __init__(self, name):
        self.name = name

    def accelerate(self):
        print(f'{self.name} is accelerating...')


string = 'Kauã'
print(string.upper())

tucson = Car('Tucson')
print(tucson.name)
tucson.accelerate()

celta = Car(name='Celta')
print(celta.name)
celta.accelerate()