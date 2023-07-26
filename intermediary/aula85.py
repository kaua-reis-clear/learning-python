my_list = []
for x in range(3):
    for y in range(3):
        my_list.append((x, y))

my_list = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
my_list = [
    [(x, letter) for letter in 'Kauã']
    for x in range(3)
]

print(my_list)