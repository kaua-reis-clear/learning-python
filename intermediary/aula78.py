# Represented by Venn diagram
# A set is mutable, but it only takes immutables for its values

# Creating a set
# set(iterable) ou {1, 2, 3}
# s1 = set('Kauã')
# s1 = set()  # empty
# s1 = {'Kauã', 1, 2, 3}  # with values

# Sets are efficient to remove duplicated values of iterables
# - Its values are always unique;
# - It doesn't take mutable values;
# - Has no indexes;
# - Doesn't ensure order;
# - It's iterable (for, in, not in)
# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# s1 = {1, 2, 3}
# print(3 not in s1)
# for number in s1:
#     print(number)

# Useful methods:
# add, update, clear, discard
# s1 = set()
# s1.add('Kauã')
# s1.add(1)
# s1.update(('Olá mundo', 1, 2, 3, 4))
# s1.discard('Olá mundo') 
# s1.discard('Kauã')
# print(s1)

# Useful operators:
# union | - unites
# intersection & - items present in both
# difference - - items present just in left set
# symmetric_difference ^ - items that are not present in both

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s1 ^ s2
print(s3)