from choice import *
from graphs import graph
from algorithms import *

if __name__ == '__main__':
    workflow = workflow()
    f = fun()
    d, e = int, float
    if workflow == 1:
        d = polynomial_degree()
    else:
        e = approximation_error()
    n = nodes_number()
    start, end = interval()
    coefficient = []
    weights, roots = laguerre(n)

    if workflow == 1:
        for i in range(0, d + 1):
            coefficient.append(lam(f, n, i, weights, roots))
        print("Blad aproksymacji wynosi: " + str(error(roots, weights, f, coefficient, n, d)))

    else:
        d = 1
        while True:
            coefficient = []
            for i in range(0, d + 1):
                coefficient.append(lam(f, n, i, weights, roots))
            if error(roots, weights, f, coefficient, n, d) <= e:
                print(f"Oczekiwany blad udalo sie uzyskac dla wielomiana stopnia: {d}")
                break
            else:
                d += 1

    calculated_x, calculated_y, real_x, real_y = [], [], [], []
    h = (end - start) / 100
    while start <= end:
        result = 0.0
        for j in range(0, d + 1):
            result += coefficient[j] * laguerre_polynomial(j, start)
        calculated_x.append(start)
        calculated_y.append(result)
        real_x.append(start)
        real_y.append(f(start))
        start += h

    graph(calculated_x, calculated_y, real_x, real_y)
