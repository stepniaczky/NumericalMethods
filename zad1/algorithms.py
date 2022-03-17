import numpy
from functions import fun1, fun2, fun3, fun4, fun5


def bisekcja(f, p, k, cond, limiter):
    if (f(p) * f(k)) < 0:
        return 'err', 'err'

    iter = 1
    while True:
        x = (p + k) / 2
        if cond == 1:
            if iter == limiter:
                return x, iter
        else:
            if abs(f(x)) < limiter:
                return x, iter

        if f(p) * f(x) > 0:
            p = x
        else:
            k = x

        iter += 1


def sieczne(f, p, k, cond, limiter):
    if (f(p) * f(k)) < 0:
        return 'err', 'err'

    iter = 1
    while True:
        x = p - (f(p) / (f(k) - f(p))) * (k - p)
        if cond == 1:
            if iter == limiter:
                return x, iter
        else:
            if abs(f(x)) < limiter:
                return x, iter

        if f(p) * f(x) > 0:
            p = x
        else:
            k = x

        iter += 1
