import math as mt
import numpy as np


def horner(arr, x):
    result = arr[0]
    for i in range(1, len(arr)):
        result *= x + arr[i]
    return result


# factorial
def fac(x): 
    result = 1
    if x == 0:
        return 1
    else:
        for i in range(1, x + 1):
            result = result * i
        return result


def laguerre_arrays(i):
    weights = []
    roots = []
    r, w = np.polynomial.laguerre.laggauss(i)
    weights.append(w)
    roots.append(r)
    return weights, roots


def laguerre_polynomial(degree, x):
    if degree == 0:
        return 1
    elif degree == 1:
        return x - 1
    else:
        L = []
        L.append(1)
        L.append(x - 1)
        for i in range(1, degree):
            L.append(((x - (2 * i) - 1) * L[i]) - (i ** 2 * L[i - 1]))
        return L[degree]


def lam(f, quadrature, degree, weights, roots):
    value = 0
    for i in range(0, quadrature):
        value += f(roots[i]) * weights[i] * laguerre_polynomial(degree, roots[i])
    return value / (fac(degree) * fac(degree))


def error(roots, weights, f, lambda_array, quadrature, degree):
    result = 0
    w = []
    for k in range(0, quadrature):
        w.append(0)
    for j in range(0, quadrature):
        for i in range(0, degree):
            w[j] = w[j] + lambda_array[i] * laguerre_polynomial(i, roots[j])
    for i in range(quadrature):
        result += weights[i] * f(roots[i] - w[i]) * f(roots[i] - w[i])
    return mt.sqrt(result)
