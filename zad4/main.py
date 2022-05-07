# Mikołaj Stępniak 236659
# Mateusz Przybył 236630
# METODY NUMERYCZNE - ZAD 4

from algorithms import Gauss, granica
from choice import funkcjaa, dokladnosc, metoda


def main():
    print("Wybierz funkcje z ponizszych \n"
          "[1]. f(x) = sin(x) \n"
          "[2]. f(x) = 2x + 1 \n"
          "[3]. f(x) = x^2 + x + 1\n"
          "[4]. f(x) = sin(2x + 1) \n")
          # "[4]. f(x) = x^4 + 2x^3 - 2x^2 - x + 4 \n")
    fun = funkcjaa()
    print("Wybierz metode \n"
          "[1]. Newton-Cotes \n"
          "[2]. Gauss-Czebyszew \n")
    met = metoda()
    if met == 1:
        eps = dokladnosc()
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("Wartosc dla Newtona-Cotesa: " + str(granica(fun, eps)))
    elif met == 2:
        i = 2
        while i != 6:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("Liczba wezlow: " + str(i))
            print("Wartosc dla Gaussa-Czebyszewa: " + str(Gauss(fun, i)))
            i += 1
    else:
        print("Blad!")
    # # OBIE METODY OBLICZANE NA RAZ:
    # print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    # print("Wartosc dla Newtona-Cotesa: " + str(granica(fun, eps)))
    # i = 2
    # while i != 6:
    #     print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    #     print("Liczba wezlow: " + str(i))
    #     print("Wartosc dla Gaussa-Czebyszewa: " + str(Gauss(fun, i)))
    #     i += 1

    return 0


if __name__ == '__main__':
    main()
