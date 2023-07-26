string = 'Kauã'
method = 'strip'

if hasattr(string, method):
    print('Has upper')
    print(getattr(string, method)())
else:
    print("It doesn't have the method", method)