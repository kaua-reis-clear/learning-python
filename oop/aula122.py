class Car:
    def __init__(self, name):
        self.name = name

    def accelerate(self):
        print(f'{self.name} is accelerating...')


tucson = Car('Tucson')
tucson.accelerate()
Car.accelerate(tucson)
# print(tucson.name)
# tucson.accelerate()

celta = Car(name='Celta')
celta.accelerate()
Car.accelerate(celta)
# print(celta.name)