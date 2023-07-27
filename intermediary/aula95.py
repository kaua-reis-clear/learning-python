def doesnt_take_zero(d):
    if d == 0:
        raise ZeroDivisionError("You're trying to divide by zero")
    return True


def must_be_int_or_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" must be int or float. '
            f'"{tipo_n.__name__}" sent.'
        )
    return True


def divide(n, d):
    must_be_int_or_float(n)
    must_be_int_or_float(d)
    doesnt_take_zero(d)
    return n / d


print(divide(8, '0'))