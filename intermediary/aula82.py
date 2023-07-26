def execute(my_function, *args):
    return my_function(*args)

# def my_sum(x, y):
#     return x + y

# def create_multiplier(multiplier):
#     def multiply(number):
#         return number * multiplier
#     return multiply

# double = create_multiplier(2)
double = execute(
    lambda m: lambda n: n * m,
    2
)

print(double(2))

print(
    execute(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)