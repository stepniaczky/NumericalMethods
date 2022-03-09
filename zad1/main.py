# zad 1 numerki d-_-b
# model 0 i 2, wariant b

import numpy


def horner(tabl, n, x):                 #
    result = tabl[0]                    #
    for i in range(1, n):               #
        result = result * x + tabl[i]   #
    return result                       #

def fun1(x):
    wartosc = x**3 - x**2 - 2*x + 1
    return wartosc

def fun2(x):
    wartosc = 2**x - 3*x
    return wartosc

def fun3(x):
    wartosc = x**3 - x + 1
    return wartosc

def fun4(x):
    wartosc = 2 + numpy.cos(2*x)
    return wartosc

def fun5(x):
    wartosc = numpy.sin(x) - numpy.cos(x)
    return wartosc

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
        print("Nieprawidlowa wartosc")
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

def menu(fun, metoda):
    if fun == 1:
        if metoda == 1:
            bisekcja()
        elif metoda == 2:
            sieczne()
    elif fun == 2:
        if metoda == 1:
            bisekcja()
        elif metoda == 2:
            sieczne()
    elif fun == 3:
        if metoda == 1:
            bisekcja()
        elif metoda == 2:
            sieczne()
    elif fun == 4:
        if metoda == 1:
            bisekcja()
        elif metoda == 2:
            sieczne()
    elif fun == 5:
        if metoda == 1:
            bisekcja()
        elif metoda == 2:
            sieczne()
    return



def main():
    fun_wybor()
