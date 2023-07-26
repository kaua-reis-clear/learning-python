# def double(number):
#     return number * 2


# def triple(number):
#     return number * 3


# def quadruple(number):
#     return number * 4
def create_multiplier(multiplier):
    def multiplicar(number):
        return number * multiplier
    return multiplicar


double = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)

print(double(2))
print(triple(2))
print(quadruple(2))