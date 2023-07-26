my_list = []
my_dict = {}
my_set = set()
my_tuple = ()
my_string = ''
my_int = 0
my_float = 0.0
my_none = None
my_false = False
my_range = range(0)

def falsy(value):
    return 'falsy'if not value else 'truthy'


print(f'TESTE', falsy('TESTE'))
print(f'{my_list=}', falsy(my_list))
print(f'{my_dict=}', falsy(my_dict))
print(f'{my_set=}', falsy(my_set))
print(f'{my_tuple=}', falsy(my_tuple))
print(f'{my_string=}', falsy(my_string))
print(f'{my_int=}', falsy(my_int))
print(f'{my_float=}', falsy(my_float))
print(f'{my_none=}', falsy(my_none))
print(f'{my_false=}', falsy(my_false))
print(f'{my_range=}', falsy(my_range))