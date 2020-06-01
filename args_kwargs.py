def myfunc(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print()

def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()

def myfunc3(*args, **kwargs):
    if args:
        for a in args:
            print(a, end=' ')
        print()
    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep='->', end=' ')
        print()

print(type(myfunc2))

values = [1, 2, 3, 5, 7, 11]
values2 = {"a": 10, "b": 20}

myfunc(values)
myfunc(*values)

myfunc(values2)
myfunc(*values2)

myfunc2(**values2)

myfunc3(10, **values2, cc=30)