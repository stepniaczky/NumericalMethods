import numpy as np
from weights_coordinates import wc
import math
from scipy.misc import derivative


def binomial_coefficient(n, k):
    return fac(n) // fac(k) // fac(n - k)


def horner(arr, x):
    result = arr[0]
    for i in range(1, len(arr)):
        result *= x + arr[i]
    return result


def fac(n):
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result


def gauss(f, nodes_number):
    result = 0
    i = 1

    while i <= nodes_number:
        actual_weight = np.pi / nodes_number
        actual_node = np.cos(((2 * i - 1) * np.pi) / (2 * nodes_number))
        result += actual_weight * f(actual_node)
        i += 1

    return result


def E(f, W, x):
    return f(x) - W(x)


def a_i(n, x):
    return (fac(n + 1) ** 2) / (laguerre_polynomial(n + 1, x) * laguerre_polynomial(n + 2, x))


def laguerre_polynomial(k, x):
    result = 0
    for m in range(k + 1):
        result += ((-1) ** m) * binomial_coefficient(k, m) * fac(m) * x ** (k - m)

    return result


#
#
# def lam(f, quadrature_polynomial, polynomialDegree, weights, roots):
#     value = 0.0
#     for i in range(0, quadrature_polynomial):
#         value += f(roots[i]) * weights[i] * laguerre_polynomial(polynomialDegree, roots[i])
#     return value / (fac(polynomialDegree) ** 2)


def approximation(mode, f, condition, n, x):
    coefficient = []

    if mode == 1:  # z okreslonym stopniem wielomianu
        weights, roots = wc[n]
        for i in range(condition + 1):
            coefficient.append(a_i(i, x))
        print(coefficient)
        # return coefficient
    else:  # z okreslonym bledem aproksymacji
        pass
