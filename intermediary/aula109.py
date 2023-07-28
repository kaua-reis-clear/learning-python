from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


people = [
    'Kauã', 'Cintia', 'André', 'Vitória',
]
shirts = [
    ['black', 'white'],
    ['p', 'm', 'g'],
    ['male', 'female', 'unisex'],
    ['cotton', 'polyester']
]

print_iter(combinations(people, 2))
print_iter(permutations(people, 2))
print_iter(product(*shirts))