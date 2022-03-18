# tu będą wszelkie wykresy
from matplotlib import pyplot as plt
import numpy as np


def graph(func, p, k, wynik, met):

    plt_precision = 0.01
    plt.xlim(p, k)
    fx = [0.0] * int((abs(p) + k) / plt_precision)
    fy = [0.0] * int((abs(p) + k) / plt_precision)
    for i in range(len(fx)):
        fx[i] = p
        fy[i] = func(p)
        p += plt_precision

    plt.scatter(wynik, func(wynik), color='red')
    # plt.plot(fx, fy, color='rebeccapurple')
    plt.grid(True)

    name = "Metoda "
    if met == 1:
        name += "bisekcji"
    else:
        name += "siecznych"

    plt.title(name)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(fx, fy, 'r')

    # plt.savefig("wykres_" + name + ".jpg", dpi=300)
    plt.show()
