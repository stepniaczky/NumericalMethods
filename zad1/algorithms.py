import numpy
from matplotlib import pyplot as plt



def horner(tabl, n, x):                 #   tabl - tablica wspolczynnikow wielomianu
    wynik = tabl[0]                     #   n - dlugosc tablicy
    for i in range(1, n):               #   x - argument
        wynik = wynik * x + tabl[i]
    return wynik


def bisekcja(funk, pocz, kon, eps):
    p = pocz
    k = kon
    i = pocz
    iteracje = 1
    fun_eps = 10e-10
    if funk(p)*funk(k) < 0:
        print("Podany przedzial jest bledny!")
        return
    while abs(funk(i)) < eps:
        srodek = (p + k)/2
        if i < kon:
            i = i + 0.1
        if abs(funk(srodek)) < fun_eps:
            return srodek
        if funk(p)*funk(srodek) > 0:
            p = srodek
        else:
            k = srodek
        iteracje += 1
    print("Liczba uzytych iteracji: ", iteracje)
    print("x = ", srodek)
    return srodek


def sieczne(funk, pocz, kon, eps):
    p = pocz
    k = kon
    i = pocz
    iteracje = 1
    fun_eps = 10e-10
    if funk(p)*funk(k) < 0:
        print("Podany przedzial jest bledny!")
        return
    while abs(funk(i)) < eps:
        pkt = (-1 * p * funk(p) * (k - p)) / (funk(k) - funk(p))  # pkt przeciecia siecznej z osia OX przez pocz i kon przedzialu
        if i < kon:
            i = i + 0.1
        if abs(funk(pkt)) < fun_eps:
            return pkt
        if funk(p)*funk(pkt) > 0:
            p = pkt
        else:
            k = pkt
        iteracje += 1
    print("Liczba uzytych iteracji: ", iteracje)
    print("x = ", pkt)
    return pkt

def bisekcja_iteracje(funk, pocz, kon, iter):
    # print(funk, pocz, kon, iter)
    p = pocz
    k = kon
    iteracje = 1
    fun_eps = 10e-10
    if funk(p) * funk(k) < 0:
        print("Podany przedzial jest bledny!")
        return
    while iteracje <= iter:
        srodek = (p + k)/2
        # print(srodek)
        if abs(funk(srodek)) < fun_eps:
            return srodek
        if funk(p)*funk(srodek) > 0:
            p = srodek
        else:
            k = srodek
        iteracje += 1
    print("Liczba uzytych iteracji: ", iteracje)
    print("x = ", srodek)
    return srodek


def sieczne_iteracje(funk, pocz, kon, iter):
    p = pocz
    k = kon
    iteracje = 1
    fun_eps = 10e-10
    if funk(p)*funk(k) < 0:
        print("Podany przedzial jest bledny!")
        return
    while iteracje <= iter:
        pkt = (-1 * p * funk(p) * (k - p)) / (funk(k) - funk(p))  # pkt przeciecia siecznej z osia OX przez pocz i kon przedzialu
        if abs(funk(pkt)) < fun_eps:
            return pkt
        if funk(p)*funk(pkt) > 0:
            p = pkt
        else:
            k = pkt
        iteracje += 1
    print("Liczba uzytych iteracji: ", iteracje)
    print("x = ", pkt)
    return pkt