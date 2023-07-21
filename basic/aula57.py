salas = [
    # 0        1
    ['Kauã', 'Vitória', ],  # 0
    # 0
    ['Léo', ],  # 1
    # 0       1       2
    ['Cintia', 'André', 'João', ],  # 2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)