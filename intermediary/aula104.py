def create_function(func):
    def internal(*args, **kwargs):
        print('I will decorate you')
        for arg in args:
            is_string(arg)
        results = func(*args, **kwargs)
        print(f'Your result was {results}.')
        print('Ok, now you have been decorated')
        return results
    return internal


@create_function
def reverse_string(string):
    print(f'{reverse_string.__name__}')
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('It must be a string')


invertida = reverse_string('123')
print(invertida)