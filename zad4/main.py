# Mikołaj Stępniak 236659
# Mateusz Przybył 236630
# METODY NUMERYCZNE - ZAD 4

import numpy as np
import math
from numpy import double


def horner(arr, x):
    result = arr[0]
    for i in range(1, len(arr)):
        result *= x + arr[i]
    return result


def funkcjaa():
    try:
        wyb = int(input("Wybor: "))
        if wyb in [1, 2, 3, 4]:
            return wyb
        else:
            print("Nie ma takiej funkcji!")
            return funkcjaa()
    except ValueError:
        print("Blad wartosci!")
        return funkcjaa()


def dokladnosc():
    try:
        eps = float(input("Podaj dokladnosc: "))
        return eps
    except ValueError:
        print("Blad wartosci!")
        return dokladnosc()


def metoda():
    try:
        met = int(input("Wybor: "))
        if met in [1, 2]:
            return met
        else:
            print("Nie ma takiej metody!")
            return metoda()
    except ValueError:
        print("Blad wartosci!")
        return metoda()


def Gauss(funkcja, iloscWezlow) -> double:
    wynik = 0
    i = 1
    while i <= iloscWezlow:
        aktualnaWaga = math.pi / iloscWezlow
        aktualnyWezel = -np.cos(((2 * i - 1) * math.pi) / (2 * iloscWezlow))
        wynik += aktualnaWaga * FX(funkcja, aktualnyWezel)
        i += 1
    return wynik


# calka wedlug wzoru Simpsona
def calka(funkcja, poczatek, koniec, eps) -> double:
    podprzedzial = 1
    delta = koniec - poczatek
    wynik = 0
    warunek = True
    while warunek:
        podprzedzial = podprzedzial * 2
        dlugosc = delta / podprzedzial
        pom = wynik  # pom - zmienna pomocnicza
        wynik = 0
        wynik += FXWX(funkcja, poczatek) + FXWX(funkcja, koniec)
        for i in range(int(podprzedzial / 2)):
            wynik += 4 * FXWX(funkcja, poczatek + (2 * i - 1) * dlugosc)
            wynik += 2 * FXWX(funkcja, poczatek + (2 * i) * dlugosc)
            i += 1
        wynik *= dlugosc / 3
        if math.fabs(pom - wynik) > eps:
            warunek = True
        else:
            warunek = False
    return wynik


# obliczamy granice w celu wyliczenia calki Newtona-Cotesa
def granica(funkcja, eps) -> double:
    wynik = 0

    # granica do +1
    poczatek = 0
    koniec = 0.5
    warunek = True
    while warunek:
        temp = calka(funkcja, poczatek, koniec, eps)
        wynik += temp
        poczatek = koniec
        koniec = koniec + ((1 - koniec) * 0.5)  # 1 / 2
        if math.fabs(temp) > eps:
            warunek = True
        else:
            warunek = False

    # granica do -1
    poczatek = -0.5
    koniec = 0
    warunek = True
    while warunek:
        temp = calka(funkcja, poczatek, koniec, eps)
        wynik += temp
        koniec = poczatek
        poczatek = poczatek - ((1 - math.fabs(koniec)) * 0.5)  # 1 / 2
        if math.fabs(temp) > eps:
            warunek = True
        else:
            warunek = False
    return wynik


def FX(funkcja, x) -> double:
    if funkcja == 1:
        return np.sin(x)
    elif funkcja == 2:
        return 2.0 * x + 1
    elif funkcja == 3:
        return horner([1, 1, 1], x)
    elif funkcja == 4:
        return np.sin(2 * x + 1)


def FXWX(funkcja, x) -> double:
    return FX(funkcja, x) * (1 / np.sqrt(1 - x * x))


def main():
    print("Wybierz funkcje z ponizszych \n"
          "[1]. f(x) = sin(x) \n"
          "[2]. f(x) = 2x + 1 \n"
          "[3]. f(x) = x^2 + x + 1\n"
          "[4]. f(x) = sin(2x + 1) \n")
    fun = funkcjaa()
    eps = dokladnosc()
    # print("Wybierz metode \n"
    #       "[1]. Newton-Cotes \n"
    #       "[2]. Gauss-Czebyszew \n")
    # met = metoda()
    # if met == 1:
    #     print("Wartosc dla Newtona-Cotesa: ")
    #     print(granica(fun, eps))
    # elif met == 2:
    #     i = 2
    #     while i != 6:
    #         print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    #         print("Liczba wezlow: " + str(i))
    #         print("Wartosc dla Gaussa-Czebyszewa: ")
    #         print(Gauss(fun, i))
    #         i += 1
    # else:
    #     print("Blad!")
    # do sprawozdania by szybciej liczyc
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Wartosc dla Newtona-Cotesa: " + str(granica(fun, eps)))
    i = 2
    while i != 6:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("Liczba wezlow: " + str(i))
        print("Wartosc dla Gaussa-Czebyszewa: " + str(Gauss(fun, i)))
        i += 1

    return 0


if __name__ == '__main__':
    main()
