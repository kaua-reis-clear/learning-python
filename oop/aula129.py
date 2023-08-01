class Class:
    @staticmethod
    def function_inside_class(*args, **kwargs):
        print('Hello', args, kwargs)


def function(*args, **kwargs):
    print('Hello', args, kwargs)


c1 = Class()
c1.function_inside_class(1, 2, 3)
function(1, 2, 3)
Class.function_inside_class(named=1)
function(named=1)