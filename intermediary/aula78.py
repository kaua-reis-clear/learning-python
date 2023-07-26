# Represented by Venn diagram
# A set is mutable, but it only takes immutables for its values

# Creating a set
# set(iterable) ou {1, 2, 3}
# s1 = set('Kauã')
s1 = set()  # empty
s1 = {'Kauã', 1, 2, 3}  # with values

# Sets are efficient to remove duplicated values of iterables
# - It doesn't take mutable values;
# - Its values are always unique;
# - Has no indexes;
# - Doesn't ensure order;
# - It's iterable (for, in, not in)

# Util methods:
# add, update, clear, discard

# Util operators:
# union - unites
# intersection - items present in both
# difference - items present just in left set
# symmetric_difference - items that are not present in both