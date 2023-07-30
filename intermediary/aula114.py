def recursive(start=0, end=4):

    print(start, end)

    # Base case
    if start >= end:
        return end

    # Recursive case
    # count until the end is reached  
    start += 1
    return recursive(start, end)


print(recursive())