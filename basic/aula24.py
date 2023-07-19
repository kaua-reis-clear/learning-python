# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3
# K A U A
# -4-3-2-1

# nome = 'Kauã'
# print('uã' in nome)
# print('ue' in nome)
# print(10 * '-')
# print('uã' not in nome)
# print('ue' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')