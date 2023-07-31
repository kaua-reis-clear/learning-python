def my_sum(a, b, /, *, c, **kwargs):
    print(kwargs)
    print(a + b + c)


my_sum(1, 2, c=3, nome='teste')