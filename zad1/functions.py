import numpy as np

arr_fn = ["f(x) = x^3 - x^2 - 2x + 1",
          "f(x) = 2^x - 3x",
          "f(x) = x^3 - x + 1",
          "f(x) = tan(x) - 1",
          "f(x) = sin(x) - cos(x)"]

def horner(tabl, n, x):                 #   tabl - tablica wspolczynnikow wielomianu
    wynik = tabl[0]                     #   n - dlugosc tablicy
    for i in range(1, n):               #   x - argument
        wynik = wynik * x + tabl[i]
    return wynik

def fun1(x): #x^3 - x^2 - 2x + 1
    tabl = [1, -1, -2, 1]
    return horner(tabl, 4, x)


def fun2(x):
    return 2**x - 3*x


def fun3(x): #x^3 - x + 1
    tabl = [1, 0, -1, 1]
    return horner(tabl, 4, x)


def fun4(x):
    return np.tan(x) - 1


def fun5(x):
    return np.sin(x) - np.cos(x)
