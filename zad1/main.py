# zad 1 numerki d-_-b
# model 0 i 2, wariant b

import numpy
from matplotlib import pyplot as plt

eps = 1

def horner(tabl, n, x):                 #
    result = tabl[0]                    #
    for i in range(1, n):               #
        result = result * x + tabl[i]   #
    return result                       #


def fun1(x):
    return x**3 - x**2 - 2*x + 1


def fun2(x):
    return 2**x - 3*x


def fun3(x):
    return x**3 - x + 1


def fun4(x):
    return 2 + numpy.cos(2*x)


def fun5(x):
    return numpy.sin(x) - numpy.cos(x)


def bisekcja(fun,pocz,kon,eps):
    p = pocz
    k = kon
    i = pocz
    fun_eps = 10e-10
    if fun(p)*fun(k) > 0:
        print("Podany przedzial jest bledny!")
        return
    while abs(fun(i)) < eps:
        srodek = (p + k)/2
        if i < kon:
            i = i + 1
        if abs(fun(srodek)) > fun_eps:
            return srodek
        if fun(p)*fun(srodek) > 0:
            pocz = srodek
        else:
            k = srodek
    return srodek


def sieczne(fun,pocz,kon,eps): #dokonczyc
    p = pocz
    k = kon
    i = pocz
    if fun(p)*fun(k) > 0:
        print("Podany przedzial jest bledny!")
        return
    while abs(fun(i)) < eps:
        #srodek
        if i < kon:
            i = i + 1
    return #srodek


def fun_wybor():
    funkcja = int
    try:
        funkcja = int(input("Prosze wybrac funkcje z ponizszej listy:\n"
                           "1. f(x) = x^3 - x^2 - 2x + 1\n"
                           "2. f(x) = 2^x - 3x\n"
                           "3. f(x) = x^3 - x + 1\n"
                           "4. f(x) = 2 + cos(2x)\n"
                           "5. f(x) = sin(x) - cos(x)\n"
                           "Wybor:"))
        met_wybor(funkcja)
    except ValueError:
        met_wybor(funkcja)
    return


def met_wybor(fun):
    if fun < 1 or fun > 5:
        print("Nieprawidlowy wybor funkcji")
        fun_wybor()
    metoda = int
    try:
        metoda = int(input("Wybierz metode:\n"
                           "1. Metoda bisekcji\n"
                           "2. Metoda sieczych\n"
                           "Wybor:"))
        menu(fun, metoda)
    except ValueError:
        met_wybor(fun)
    return


def przedzial():
    pocz = int
    kon = int
    try:
        pocz = int(input("Podaj poczatek przedzialu:\n"
                     ""))
    except ValueError:
        print("Wprowadzono nieodpowiedni znak")

    try:
        kon = int(input("Podaj koniec przedzialu:\n"
                     ""))
    except ValueError:
        print("Wprowadzono nieodpowiedni znak")
    if (pocz > kon):
        print("Przedzial nieprawidlowo wprowadzony (poczatek przedzialu > koniec przedzialu)")
        przedzial()
    return pocz, kon


def menu(fun, metoda):
    if metoda < 1 or metoda > 2:
        print("Nieprawidlowy wybor metody")
        met_wybor(fun)
    pocz, kon = przedzial()
    if metoda == 1:
        if fun == 1:
            bisekcja(fun1(),pocz,kon,eps)
        elif fun == 2:
            bisekcja(fun2(),pocz,kon,eps)
        elif fun == 3:
            bisekcja(fun3(),pocz,kon,eps)
        elif fun == 4:
            bisekcja(fun4(),pocz,kon,eps)
        elif fun == 5:
            bisekcja(fun5(),pocz,kon,eps)
    elif metoda == 2:
        if fun == 1:
            sieczne(fun1(),pocz,kon,eps)
        elif fun == 2:
            sieczne(fun2(),pocz,kon,eps)
        elif fun == 3:
            sieczne(fun3(),pocz,kon,eps)
        elif fun == 4:
            sieczne(fun4(),pocz,kon,eps)
        elif fun == 5:
            sieczne(fun5(),pocz,kon,eps)
    return


def main():
    fun_wybor()

main()
