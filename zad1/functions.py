import numpy

def fun1(x): #x^3 - x^2 - 2x + 1
    tabl = [1, -1, -2, 1]
    return horner(tabl, 4, x)


def fun2(x):
    return 2**x - 3*x


def fun3(x): #x^3 - x + 1
    tabl = [1, 0, -1, 1]
    return horner(tabl, 4, x)


def fun4(x):
    return 2 + numpy.cos(2*x)


def fun5(x):
    return numpy.sin(x) - numpy.cos(x)
