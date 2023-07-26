letters = set()

while True:
    letter = input('Type: ')
    letters.add(letter)

    if 'l' in letters:
        print('CONGRATULATIONS')
        break
    
print(letters)