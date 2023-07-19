"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal
"""

nome = 'Kauã'
preco = 1000.41421421
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))