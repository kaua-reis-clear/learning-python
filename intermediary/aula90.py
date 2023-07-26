import sys

iterable = ['I', 'have', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
my_list = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(my_list))
print(sys.getsizeof(generator))

print(generator)

# for n in generator:
#     print(n)