from numpy import double
from functions import functions, human_readable_functions


def workflow():
    print("1. Tryb z okresleniem stopnia wielomianu",
          "2. Tryb z okresleniem bledu aproksymacji", sep="\n")
    try:
        choice = int(input("Tryb pracy: "))
        if choice in [1, 2]:
            return choice
        print("Prosze wybrac tryb z zakresu: 1/2!")
    except ValueError:
        print("Wprowadzono niepoprawna wartosc!")

        return workflow()


def fun():
    try:
        for key in human_readable_functions:
            print(f"{key}: {human_readable_functions[key]}")
        choice = int(input("Wybierz funkcje: "))
        if choice in functions.keys():
            return functions[choice]
        print("Prosze wybrac funkcje z wyswietlonego zakresu:")
    except ValueError:
        print("Wprowadzono nieprawidlowa wartosc!")

    return fun()


def interval():
    try:
        start = double(input("Podaj poczatek przedzialu: "))
        end = double(input("Podaj koniec przedzialu: "))
        if start < end:
            return start, end
        print("Przedzial nieprawidlowo wprowadzony "
              "(poczatek przedzialu > koniec przedzialu).")
    except ValueError:
        print("Wprowadzono nieprawidlowa wartosc!")

    return interval()


def polynomial_degree():
    try:
        choice = int(input("Stopien wielomianu aproksymujacego: "))
        if choice > 0:
            return choice
        print("Prosze wybrac liczbe wieksza od 0!")
    except ValueError:
        print("Wprowadzono nieprawidlowa wartosc!")

    return polynomial_degree()


def nodes_number():
    try:
        choice = int(input("Liczba wezlow (2 - 5): "))
        if choice in [2, 3, 4, 5]:
            return choice
        print("Prosze wybrac liczbe z przedzialu: 2 - 5!")
    except ValueError:
        print("Wprowadzono nieprawidlowa wartosc!")

    return nodes_number()


def approximation_error():
    try:
        choice = int(input("Oczekiwany blad aproksymacji: "))
        if choice > 0:
            return choice
        print("Wybrany blad musi byc wiekszy od 0!")
    except ValueError:
        print("Wprowadzono nieprawidlowa wartosc!")

    return approximation_error()
