def create_function(func):
    def internal(*args, **kwargs):
        print('I will decorate you')
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        print(f'Your result was {result}.')
        print('Ok, now you have been decorated')
        return result
    return internal


def reverse_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('It must be a string')


reverse_string_checking_parameter = create_function(reverse_string)
reversed = reverse_string_checking_parameter('123')
print(reversed)