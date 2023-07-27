def sum(x, y):
    return x + y
def multiply(x, y):
    return x * y


def create_function(function, x):
    def internal(y):
        return function(x, y)
    return internal


plus_five = create_function(sum, 5)
five_times = create_function(multiply, 10)

print(plus_five(10))
print(five_times(10))