# x, y, *rest = 1, 2, 3, 4
# print(x, y, rest)


# def sum(x, y):
#     return x + y

def sum(*args):
    total = 0
    for numero in args:
        total += numero
    return total


sum_1_2_3 = sum(1, 2, 3)
# print(sum_1_2_3)

sum_4_5_6 = sum(4, 5, 6)
# print(sum_4_5_6)

numbers = 1, 2, 3, 4, 5, 6, 7, 78, 10
other_sum = sum(*numbers)
print(other_sum)

print(sum(numbers))
# print(*numbers)