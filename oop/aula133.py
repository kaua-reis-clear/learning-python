from functools import partial


class Foo:
    def __init__(self):
        self.public = 'this is public'
        self._protected = 'this is protected'
        self.__example = 'this is private'

    def public_method(self):
        # self._protected_method()
        # print(self._protected)
        print(self.__example)
        self.__private_method()
        return 'public_method'

    def _protected_method(self):
        print('_protected_method')
        return '_protected_method'

    def __private_method(self):
        print('__private_method')
        return '__private_method'


f = Foo()
# print(f.public)
print(f.public_method())