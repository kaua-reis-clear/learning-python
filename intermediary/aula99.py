from sys import path

import aula99_package.modulo
from aula99_package import modulo
from aula99_package.modulo import *

# from aula99_package.modulo import module_sum

# print(*path, sep='\n')
print(module_sum(1, 2))
print(aula99_package.modulo.module_sum(1, 2))
print(modulo.module_sum(1, 2))
print(variable)
print(new_variable)