from numpy import double as np
from functions import functions, human_readable_functions


def fun():
    try:
        for key in human_readable_functions:
            print(f"{key}: {human_readable_functions[key]}")
        choice = int(input("Wybierz funkcje: "))
        if choice in functions.keys():
            return choice
        print("Prosze wybrac funkcje z wyswietlonego zakresu!")
    except ValueError:
        print("Wprowadzono nieprawidlowa wartosc!")

    return fun()


def interval():
    try:
        start = np.double(input("Podaj poczatek przedzialu: "))
        end = np.double(input("Podaj koniec przedzialu: "))
        if start < end:
            return start, end
        print("Przedzial nieprawidlowo wprowadzony "
              "(poczatek przedzialu > koniec przedzialu).")
    except ValueError:
        print("Wprowadzono nieprawidlowa wartosc!")

    return interval()


def nodes_number():
    try:
        choice = int(input("Liczba wezlow interpolacyjnych: "))
        if choice > 0:
            return choice
        print("Prosze wybrac liczbe wieksza od 0!")
    except ValueError:
        print("Wprowadzono nieprawidlowa wartosc!")

    return nodes_number()
