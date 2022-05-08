import numpy as np
import math
from numpy import double

przedzial = [-1, 1]


def suma_I(n, funkcja):
    poczatek = przedzial[0]
    koniec = przedzial[1]
    suma = 0
    coil_ex = abs(poczatek - koniec) / n
    for i in range(1, n):
        x = poczatek + (coil_ex * i)
        suma += FX(funkcja, x)
    return suma


def suma_T(n, funkcja):
    poczatek = przedzial[0]
    koniec = przedzial[1]
    suma = 0
    coil_e = abs(poczatek - koniec) / n
    poczatek_T = poczatek - (coil_e / 2)
    for i in range(1, n + 1):
        x = poczatek_T + (coil_e * i)
        suma += FX(funkcja, x)
    return suma


def newton_cotes(n, funkcja):
    poczatek = przedzial[0]
    koniec = przedzial[1]
    return (koniec - poczatek) / (6 * n) * (FX(funkcja, poczatek) + FX(funkcja, koniec)
                                            + (2 * suma_I(n, funkcja)) + (4 * suma_T(n, funkcja)))


def horner(arr, x):
    result = arr[0]
    for i in range(1, len(arr)):
        result *= x + arr[i]
    return result


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

    # n = 1
    # while True:
    #     wynik_wczes = wynik
    #     wynik = newton_cotes(n, funkcja)
    #     if abs(wynik - wynik_wczes) <= eps:
    #         break
    #     n += 1

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

    # while True:
    #     wynik_wczes = wynik
    #     wynik = newton_cotes(n, funkcja)
    #     if abs(wynik - wynik_wczes) <= eps:
    #         break
    #     n += 1

    return wynik


def FX(funkcja, x) -> double:
    if funkcja == 1:
        return np.sin(x)
    elif funkcja == 2:
        return 2.0 * x + 1
    elif funkcja == 3:
        return horner([1, 1, 1], x)
    elif funkcja == 4:
        return np.arcsin(x)


def FXWX(funkcja, x) -> double:
    return FX(funkcja, x) * (1 / np.sqrt(1 - x * x))
