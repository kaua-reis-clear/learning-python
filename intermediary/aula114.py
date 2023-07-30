# import sys

# sys.setrecursionlimit(1004)


# def recursive(start=0, end=4):

#     print(start, end)

#     # Base case
#     if start >= end:
#         return end

#     # Recursive case
#     # count until reach the end
#     start += 1
#     return recursive(start, end)


# print(recursive(0, 1001))

def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))
print(factorial(10))
print(factorial(100))