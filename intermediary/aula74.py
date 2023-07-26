def create_greeting(greeting):
    def saudar(name):
        return f'{greeting}, {name}!'
    return saudar


say_good_morning = create_greeting('Good morning')
say_good_night = create_greeting('Good night')

for name in ['Kauã', 'Cintia', 'André']:
    print(say_good_morning(name))
    print(say_good_night(name))