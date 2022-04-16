from numpy import double


def horner(arr, x):
    result = arr[0]
    for i in range(1, len(arr)):
        result *= x + arr[i]
    return result


def get_nodes(f, n, start, end):
    fx, fy = [], []
    dist = end - start
    h = dist / (n - 1)

    for i in range(n):
        fx.append(start)
        fy.append(f(start))
        start += h

    return fx, fy, h


def fac(n):
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result


def binomial_coefficient(n, k):
    return fac(n) // fac(k) // fac(n - k)


def progressive_diff(f, i: int, fx):
    result = 0
    for k in range(0, i + 1):
        result += (-1) ** (i - k) * binomial_coefficient(i, k) * f(fx[k])
    return result


def t(x, x0, h) -> double:
    return (x - x0) / h


def newton_interpolation(f, fx, x) -> double:
    multiplier = 1
    Wt = f(fx[0])
    h = fx[1] - fx[0]

    for i in range(1, len(fx)):
        multiplier *= t(x, fx[0], h) - (i - 1)
        a_i = progressive_diff(f, i, fx) / fac(i)
        Wt += a_i * multiplier

    return Wt
