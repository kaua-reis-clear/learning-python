def gen1():
    print('GEN1 STARTED')
    yield 1
    yield 2
    yield 3
    print('GEN1 FINISHED ')


def gen3():
    print('GEN3 STARTED')
    yield 10
    yield 20
    yield 30
    print('GEN3 FINISHED')


def gen2(gen=None):
    print('GEN2 STARTED')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('GEN2 FINISHED')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()
for number in g1:
    print(number)
print()
for number in g2:
    print(number)
print()
for number in g3:
    print(number)
print()