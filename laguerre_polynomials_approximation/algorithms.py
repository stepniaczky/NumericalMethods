import numpy as np
import math


def horner(arr, x):
    result = arr[0]
    for i in range(1, len(arr)):
        result *= x + arr[i]
    return result


def binomial_coefficient(n, k):
    return fac(n) // fac(k) // fac(n - k)


def fac(x):
    result = 1
    if x == 0:
        return 1
    else:
        for i in range(1, x + 1):
            result = result * i
        return result


def gauss(iloscWezlow) -> tuple:
    weights = []
    roots = []
    i = 1
    while i <= iloscWezlow:
        aktualnaWaga = math.pi / iloscWezlow
        aktualnyWezel = -np.cos(((2 * i - 1) * math.pi) / (2 * iloscWezlow))
        weights.append(aktualnaWaga)
        roots.append(aktualnyWezel)
        i += 1
    return weights, roots


def laguerre(n):
    weights = []
    roots = []
    r, w = np.polynomial.laguerre.laggauss(n)
    weights.append(w)
    roots.append(r)
    return weights[0], roots[0]


def laguerre_polynomial(degree, x):
    if degree == 0:
        return 1
    elif degree == 1:
        return x - 1
    else:
        L = [1, x - 1]
        for i in range(1, degree):
            L.append(((x - (2 * i) - 1) * L[i]) - (i ** 2 * L[i - 1]))
        return L[degree]


def lam(f, quadrature, degree, weights, roots):
    value = 0
    for i in range(0, quadrature):
        value += f(roots[i]) * weights[i] * laguerre_polynomial(degree, roots[i])
    return value / (fac(degree) ** 2)


def error(roots, weights, f, coefficient, quadrature, degree):
    err = 0
    F = []
    for k in range(quadrature):
        F.append(0)
    for j in range(quadrature):
        for i in range(0, degree):
            F[j] = F[j] + coefficient[i] * laguerre_polynomial(i, roots[j])
    for i in range(quadrature):
        err = err + weights[i] * ((f(roots[i]) - F[i]) ** 2)
    return math.sqrt(err)
