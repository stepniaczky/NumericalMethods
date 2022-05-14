# Wariant 3: wielomiany Laguerre'a
from choice import workflow, fun, interval, polynomial_degree, nodes_number, approximation_error
from algorithms import *
from graphs import graph

if __name__ == '__main__':

    # initial setup
    mode = workflow()
    function = fun()
    start, end = interval()
    n = nodes_number()
    condition = polynomial_degree() if mode == 1 else approximation_error()

    approximation(mode, function, condition, n, 2.1)
    #
    # calculated_x, calculated_y, real_x, real_y = [], [], [], []
    # h = (end - start) / 100
    # while start <= end:
    #     result = 0.0
    #     for j in range(0, condition + 1):
    #         result += coefficient[j] * laguerre_polynomial(j, start)
    #     calculated_x.append(start)
    #     calculated_y.append(result)
    #     real_x.append(start)
    #     real_y.append(function(start))
    #     start += h
    #
    # # graph(fx, fy, calculated_x, calculated_y, real_x, real_y)
    # graph(calculated_x, calculated_y, real_x, real_y)
