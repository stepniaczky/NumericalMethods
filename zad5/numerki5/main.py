from choice import *
from graphs import graph
from algorithms import *

if __name__ == '__main__':
    f = fun()
    d = polynomial_degree()
    n = nodes_number()
    start, end = interval()
    coefficient = []
    weights, roots = laguerre_arrays(n)
    for i in range(0, d + 1):
        err = lam(f, n, i, weights[0], roots[0])
        coefficient.append(err)
        print("x" + str(d - i) + ": " + str(err))
    print("Blad aproksymacji wynosi: " + str(error(roots[0], weights[0],
                                                  f, coefficient, n, d)))
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

    # graph(fx, fy, calculated_x, calculated_y, real_x, real_y)
    graph(calculated_x, calculated_y, real_x, real_y)