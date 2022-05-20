# Wariant 4: Newtona dla węzłów równoodległych
from choice import fun, interval, nodes_number
from algorithms import get_nodes, newton_interpolation
from graphs import graph

if __name__ == '__main__':

    function = fun()
    start, end = interval()
    n = nodes_number()
    fx, fy, h = get_nodes(function, n, start, end)

    calculated_x, calculated_y, real_x, real_y = [], [], [], []
    h /= 100
    while start <= end:
        calculated_x.append(start)
        calculated_y.append(newton_interpolation(function, fx, start))
        real_x.append(start)
        real_y.append(function(start))
        start += h

    average_err = (sum(real_y) - sum(calculated_y)) / len(calculated_y)
    print(f"Blad przyblizonej wartosci funkcji f(x): {average_err}")
    graph(fx, fy, calculated_x, calculated_y, real_x, real_y)

