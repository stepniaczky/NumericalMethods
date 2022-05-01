# Mikołaj Stępniak 236659
# Mateusz Przybył 236630
# METODY NUMERYCZNE - ZAD 4

import numpy as np
import math

PI = 3.141592653589793238462643383279502884


def horner(arr, x):
    result = arr[0]
    for i in range(1, len(arr)):
        result *= x + arr[i]
    return result


def wybor_funkcji():
    try:
        choice = int(input("Wybor: "))
        if choice in [1, 2, 3, 4]:
            return choice
        else:
            print("Nie ma takiej funkcji!")
            return wybor_funkcji()
    except ValueError:
        print("Blad wartosci!")
        return wybor_funkcji()


def dokladnosc():
    try:
        acc = float(input("Podaj dokladnosc: "))
        return acc
    except ValueError:
        print("Blad wartosci!")
        return dokladnosc()


def Gauss(funkcja, iloscWezlow):
    wynik = 0
    for i in range(iloscWezlow):
        aktualnaWaga = PI / iloscWezlow
        aktualnyWezel = -np.cos(((2 * i - 1) * PI) / (2 * iloscWezlow))
        wynik += aktualnaWaga * FX(funkcja, aktualnyWezel)
    return wynik


# calka Simpsona
def calka(funkcja, poczatek, koniec, eps):
    podprzedzial = 1
    delta = koniec - poczatek
    wynik = 0
    while math.fabs(pom - wynik) > eps:
        podprzedzial = podprzedzial * 2
        dlugosc = delta / podprzedzial
        pom = wynik  # pom - zmienna pomocnicza
        wynik = 0
        wynik += FXWX(funkcja, poczatek) + FXWX(funkcja, koniec)
        for i in range(podprzedzial / 2):
            wynik += 4 * FXWX(funkcja, poczatek + (2 * i - 1) * dlugosc)
            wynik += 2 * FXWX(funkcja, poczatek + (2 * i) * dlugosc)
            i += 1
        wynik *= dlugosc / 3
    return wynik


def FX(funkcja, x):
    if funkcja == 1:
        return np.sin(x)
    elif funkcja == 2:
        return 2.0 * x + 1
    elif funkcja == 3:
        return horner([1, 0, 3, 0, 1], x)
    elif funkcja == 4:
        return np.cos(x)


def FXWX(funkcja, x):
    return FX(funkcja, x) * (1 / np.sqrt(1 - x ** 2))


# wartosci funkcji z waga
functions = {
    1: lambda x: np.sin(x) * (1 / np.sqrt(1 - x ** 2)),
    2: lambda x: (2.0 * x - 1) * (1 / np.sqrt(1 - x ** 2)),
    3: lambda x: horner([1, 0, 3, 0, 1], x) * (1 / np.sqrt(1 - x ** 2)),
    4: lambda x: np.cos(x) * (1 / np.sqrt(1 - x ** 2))
}

# wartosci funkcji
raw_functions = {
    1: lambda x: np.sin(x),
    2: lambda x: (2.0 * x + 1),
    3: lambda x: horner([1, 0, 3, 0, 1], x),
    4: lambda x: np.cos(x)
}


def main():
    print("Wybierz funkcje z ponizszych \n"
          "[1]. f(x) = sin(x) \n"
          "[2]. f(x) = 2x + 1 \n"
          "[3]. f(x) = x^4 + 3x^2 + 1 \n"
          "[4]. f(x) = cos(x) \n")
    fun = wybor_funkcji()
    eps = dokladnosc()
    i = 2
    while i != 6:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("Liczba wezlow: " + str(i))
        print("Wartosc dla Gaussa-Czebyszewa: ")
        print(Gauss(fun, i))
        i += 1


if __name__ == '__main__':
    main()
