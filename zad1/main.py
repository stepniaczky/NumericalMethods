# zad 1 numerki d-_-b
# model 0 i 2, wariant b

#   TO DO LIST
# - bisekcja, sprawdzenie czy dobrze dziala
# - metoda siecznych, napisanie jej xd      CHECK
# - metoda siecznych, sprawdzenie czy dziala tak jak trzeba
# - wykresy
# - w metodzie menu() problem z przekazaniem funkcji funX() [X = 1, 2, ..., 5]

import numpy
from matplotlib import pyplot as plt



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
    tabl = [1, -1, 1]
    return horner(tabl, 3, x)


def fun4(x):
    return 2 + numpy.cos(2*x)


def fun5(x):
    return numpy.sin(x) - numpy.cos(x)


def bisekcja(fun, pocz, kon, eps):
    p = pocz
    k = kon
    i = pocz
    iteracje = 1
    fun_eps = 10e-10
    if fun(p)*fun(k) > 0:
        print("Podany przedzial jest bledny!")
        return
    while abs(fun(i)) < eps:
        srodek = (p + k)/2
        if i < kon:
            i = i + 1
        if abs(fun(srodek)) < fun_eps:
            return srodek
        if fun(p)*fun(srodek) > 0:
            p = srodek
        else:
            k = srodek
        iteracje += 1
    print("Liczba uzytych iteracji: ", iteracje)
    return srodek


def sieczne(fun, pocz, kon, eps):
    p = pocz
    k = kon
    i = pocz
    iteracje = 1
    fun_eps = 10e-10
    if fun(p)*fun(k) > 0:
        print("Podany przedzial jest bledny!")
        return
    while abs(fun(i)) < eps:
        pkt = (-1 * p * fun(p) * (k - p)) / (fun(k) - fun(p))  # pkt przeciecia siecznej z osia OX przez pocz i kon przedzialu
        if i < kon:
            i = i + 1
        if abs(fun(pkt)) < fun_eps:
            return pkt
        if fun(p)*fun(pkt) > 0:
            p = pkt
        else:
            k = pkt
        iteracje += 1
    print("Liczba uzytych iteracji: ", iteracje)
    return pkt

def bisekcja_iteracje(fun, pocz, kon, iter):
    p = pocz
    k = kon
    i = pocz
    iteracje = 1
    fun_eps = 10e-10
    if fun(p)*fun(k) > 0:
        print("Podany przedzial jest bledny!")
        return
    while iteracje <= iter:
        srodek = (p + k)/2
        if i < kon:
            i = i + 1
        if abs(fun(srodek)) < fun_eps:
            return srodek
        if fun(p)*fun(srodek) > 0:
            p = srodek
        else:
            k = srodek
        iteracje += 1
    print("Liczba uzytych iteracji: ", iteracje)
    return srodek


def sieczne_iteracje(fun, pocz, kon, iter):
    p = pocz
    k = kon
    i = pocz
    iteracje = 1
    fun_eps = 10e-10
    if fun(p)*fun(k) > 0:
        print("Podany przedzial jest bledny!")
        return
    while iteracje <= iter:
        pkt = (-1 * p * fun(p) * (k - p)) / (fun(k) - fun(p))  # pkt przeciecia siecznej z osia OX przez pocz i kon przedzialu
        if i < kon:
            i = i + 1
        if abs(fun(pkt)) < fun_eps:
            return pkt
        if fun(p)*fun(pkt) > 0:
            p = pkt
        else:
            k = pkt
        iteracje += 1
    print("Liczba uzytych iteracji: ", iteracje)
    return pkt


def fun_wybor():
    funkcja = int
    try:
        funkcja = int(input("Prosze wybrac funkcje z ponizszej listy:\n"
                           "1. f(x) = x^3 - x^2 - 2x + 1,\n"
                           "2. f(x) = 2^x - 3x,\n"
                           "3. f(x) = x^3 - x + 1,\n"
                           "4. f(x) = 2 + cos(2x),\n"
                           "5. f(x) = sin(x) - cos(x).\n"
                           "Wybor: "))
        met_wybor(funkcja)
    except ValueError:
        met_wybor(funkcja)
    return


def met_wybor(fun):
    if fun < 1 or fun > 5:
        print("Nieprawidlowy wybor funkcji.")
        fun_wybor()
    metoda = int
    try:
        metoda = int(input("Wybierz metode:\n"
                           "1. Metoda bisekcji,\n"
                           "2. Metoda sieczych.\n"
                           "Wybor: "))
        menu(fun, metoda)
    except ValueError:
        met_wybor(fun)
    return


def przedzial():
    pocz = int
    kon = int
    try:
        pocz = int(input("Podaj poczatek przedzialu: "))
    except ValueError:
        print("Wprowadzono nieodpowiedni znak.")
    try:
        kon = int(input("Podaj koniec przedzialu: "))
    except ValueError:
        print("Wprowadzono nieodpowiedni znak.")
    if pocz > kon:
        print("Przedzial nieprawidlowo wprowadzony (poczatek przedzialu > koniec przedzialu).")
        przedzial()
    return pocz, kon


# def warunek():
#     wybor = int
#     try:
#         wybor = int(input("Algorytm ma zakonczyc sie:\n"
#                           "1. Po osiagnieciu okreslonego eps,\n"
#                           "2. Po osiagnieciu okreslinej liczby iteracji.\n"
#                           "Wybor: "))
#     except ValueError:
#         print("Wprowadzono nieodpowiedni znak.")
#     if wybor < 1 or wybor > 2:
#         warunek()
#     if wybor == 1:
#         eps = double
#         try:
#             eps = double(input("Podaj wartosc eps: "))
#         except ValueError:
#             print("Wprowadzono nieodpowiedni znak.")
#         return eps
#
#     elif wybor == 2:

def menu(fun, metoda):
    if metoda < 1 or metoda > 2:
        print("Nieprawidlowy wybor metody.")
        met_wybor(fun)

    warunek = int
    try:
        warunek = int(input("Algorytm ma zakonczyc sie gdy:\n"
                            "1.Zostanie osiagnieta podana liczba iteracji,\n"
                            "2.Zostanie osiagnieta podana wartosc eps.\n"
                            "Wybor: "))
    except ValueError:
        print("Wprowadzono nieodpowiedni znak.")
    if warunek < 1 or warunek > 2:
        menu(fun,metoda)

    if warunek == 1:
        iteracje = int
        try:
            iteracje = int(input("Podaj maksymalna liczbe iteracji: "))
        except ValueError:
            print("Wprowadzono nieodpowiedni znak.")
        pocz, kon = przedzial()
        if metoda == 1:
            if fun == 1:
                bisekcja_iteracje(fun1(), pocz, kon, iteracje)
            elif fun == 2:
                bisekcja_iteracje(fun2(), pocz, kon, iteracje)
            elif fun == 3:
                bisekcja_iteracje(fun3(), pocz, kon, iteracje)
            elif fun == 4:
                bisekcja_iteracje(fun4(), pocz, kon, iteracje)
            elif fun == 5:
                bisekcja_iteracje(fun5(), pocz, kon, iteracje)
        elif metoda == 2:
            if fun == 1:
                sieczne_iteracje(fun1(), pocz, kon, iteracje)
            elif fun == 2:
                sieczne_iteracje(fun2(), pocz, kon, iteracje)
            elif fun == 3:
                sieczne_iteracje(fun3(), pocz, kon, iteracje)
            elif fun == 4:
                sieczne_iteracje(fun4(), pocz, kon, iteracje)
            elif fun == 5:
                sieczne_iteracje(fun5(), pocz, kon, iteracje)

    elif warunek == 2:
        eps = numpy.double
        try:
            eps = numpy.double(input("Podaj wartosc eps: "))
        except ValueError:
            print("Wprowadzono nieodpowiedni znak.")
        pocz, kon = przedzial()
        if metoda == 1:
            if fun == 1:
                bisekcja(fun1(), pocz, kon, eps)
            elif fun == 2:
                bisekcja(fun2(), pocz, kon, eps)
            elif fun == 3:
                bisekcja(fun3(), pocz, kon, eps)
            elif fun == 4:
                bisekcja(fun4(), pocz, kon, eps)
            elif fun == 5:
                bisekcja(fun5(), pocz, kon, eps)
        elif metoda == 2:
            if fun == 1:
                sieczne(fun1(), pocz, kon, eps)
            elif fun == 2:
                sieczne(fun2(), pocz, kon, eps)
            elif fun == 3:
                sieczne(fun3(), pocz, kon, eps)
            elif fun == 4:
                sieczne(fun4(), pocz, kon, eps)
            elif fun == 5:
                sieczne(fun5(), pocz, kon, eps)


def main():
    fun_wybor()


main()