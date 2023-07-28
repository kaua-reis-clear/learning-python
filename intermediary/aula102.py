# Variáveis livres + nonlocal (locals, globals)
# print(globals())
# def outside(x):
#     a = x

#     def inside():
#         # print(locals())

#         return a
#     return inside


# inside1 = outside(10)
# inside2 = outside(20)

# print(inside1())
# print(inside2())
def concat(initial_string):
    final_value = initial_string

    def internal(value_to_concat=''):
        nonlocal final_value
        final_value += value_to_concat
        return final_value
    return internal


c = concat('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)