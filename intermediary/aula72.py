def multiply(*args):
    total = 1
    for number in args:
        total *= number
    return total


multiplication = multiply(10, 2, 3, 4, 5)
print(multiplication)


def odd_even(number):
    multiple_of_two = number % 2 == 0

    if multiple_of_two:
        return f'{number} é even'
    return f'{number} é odd'


other_odd_even = odd_even
two_is_even = other_odd_even(2)
print(two_is_even)
print(odd_even(3))
print(odd_even(15))
print(odd_even(16))

print(odd_even is other_odd_even)