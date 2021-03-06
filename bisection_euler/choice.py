from numpy import double
from functions import arr_fn

def fun_choice():
    try:
        print("Prosze wybrac funkcje z ponizszej listy:")
        for i in range(len(arr_fn)):
            print(f'{i + 1}.', arr_fn[i])
        choice = int(input("Wybor: "))

        if choice in [1, 2, 3, 4, 5]:
            return choice
        print("Prosze wybrac funkcje z wyswietlonego zakresu!")
    except ValueError:
        print("Wprowadzono nieprawidlowa wartosc!")

    return fun_choice()


def met_choice():
    try:
        choice = int(input("Wybierz metode:\n"
                           "1. Metoda bisekcji,\n"
                           "2. Metoda sieczych.\n"
                           "Wybor: "))
        if choice in [1, 2]:
            return choice
        print("Prosze wybrac metode z wyswietlonego zakresu!")
    except ValueError:
        print("Wprowadzono nieprawidlowa wartosc!")

    return met_choice()


def przedzial():
    pocz, kon = 1, 0

    while pocz > kon:
        try:
            pocz = double(input("Podaj poczatek przedzialu: "))
            kon = double(input("Podaj koniec przedzialu: "))
            if pocz < kon:
                return pocz, kon
            print("Przedzial nieprawidlowo wprowadzony "
                  "(poczatek przedzialu > koniec przedzialu).")
        except ValueError:
            print("Wprowadzono nieprawidlowa wartosc!")
            pocz, kon = 1, 0



def condition():
    cond = int

    while cond not in [1, 2]:
        try:
            cond = int(input("Algorytm ma zakonczyc sie gdy:\n"
                                "1.Zostanie osiagnieta podana liczba iteracji,\n"
                                "2.Zostanie osiagnieta podana wartosc eps.\n"
                                "Wybor: "))
        except ValueError:
            print("Wprowadzono nieprawidlowa wartosc!")

    if cond == 1:
        iteracje = 0
        while iteracje <= 0:
            try:
                iteracje = int(input("Podaj maksymalna liczbe iteracji: "))
            except ValueError:
                print("Wprowadzono nieprawidlowa wartosc!")
        return cond, iteracje

    else:
        eps = 0
        while eps <= 0:
            try:
                eps = double(input("Podaj wartosc eps: "))
            except ValueError:
                print("Wprowadzono nieprawidlowa wartosc!")
        return cond, eps
