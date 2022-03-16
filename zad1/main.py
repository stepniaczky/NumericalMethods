# zad 1 numerki d-_-b
# model 0 i 2, wariant b

#   TO DO LIST
# - bisekcja, sprawdzenie czy dobrze dziala
# - metoda siecznych, napisanie jej xd      CHECK
# - metoda siecznych, sprawdzenie czy dziala tak jak trzeba
# - wykresy
# - w metodzie menu() problem z przekazaniem funkcji funX() [X = 1, 2, ..., 5]


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
        fun_wybor()
    return


def met_wybor(funk):
    # print(funk)
    if funk < 1 or funk > 5:
        print("Nieprawidlowy wybor funkcji.")
        fun_wybor()
    metoda = int
    try:
        metoda = int(input("Wybierz metode:\n"
                           "1. Metoda bisekcji,\n"
                           "2. Metoda sieczych.\n"
                           "Wybor: "))
        menu(funk, metoda)
    except ValueError:
        met_wybor(funk)
    return


def przedzial():
    pocz = float
    kon = float
    try:
        pocz = float(input("Podaj poczatek przedzialu: "))
    except ValueError:
        print("Wprowadzono nieodpowiedni znak.")
    try:
        kon = float(input("Podaj koniec przedzialu: "))
    except ValueError:
        print("Wprowadzono nieodpowiedni znak.")
    if pocz > kon:
        print("Przedzial nieprawidlowo wprowadzony (poczatek przedzialu > koniec przedzialu).")
        przedzial()
    return pocz, kon


def menu(funk, metoda):
    if metoda < 1 or metoda > 2:
        print("Nieprawidlowy wybor metody.")
        met_wybor(funk)

    warunek = int
    try:
        warunek = int(input("Algorytm ma zakonczyc sie gdy:\n"
                            "1.Zostanie osiagnieta podana liczba iteracji,\n"
                            "2.Zostanie osiagnieta podana wartosc eps.\n"
                            "Wybor: "))
    except ValueError:
        print("Wprowadzono nieodpowiedni znak.")
    if warunek < 1 or warunek > 2:
        menu(funk, metoda)

    if warunek == 1:
        iteracje = int
        try:
            iteracje = int(input("Podaj maksymalna liczbe iteracji: "))
        except ValueError:
            print("Wprowadzono nieodpowiedni znak.")
        pocz, kon = przedzial()
        # print(pocz, kon)
        if metoda == 1:
            if funk == 1:
                bisekcja_iteracje(fun1, pocz, kon, iteracje)
            elif funk == 2:
                bisekcja_iteracje(fun2, pocz, kon, iteracje)
            elif funk == 3:
                bisekcja_iteracje(fun3, pocz, kon, iteracje)
            elif funk == 4:
                bisekcja_iteracje(fun4, pocz, kon, iteracje)
            elif funk == 5:
                bisekcja_iteracje(fun5, pocz, kon, iteracje)
        elif metoda == 2:
            if funk == 1:
                sieczne_iteracje(fun1, pocz, kon, iteracje)
            elif funk == 2:
                sieczne_iteracje(fun2, pocz, kon, iteracje)
            elif funk == 3:
                sieczne_iteracje(fun3, pocz, kon, iteracje)
            elif funk == 4:
                sieczne_iteracje(fun4, pocz, kon, iteracje)
            elif funk == 5:
                sieczne_iteracje(fun5, pocz, kon, iteracje)

    elif warunek == 2:
        eps = float
        try:
            eps = float(input("Podaj wartosc eps: "))
        except ValueError:
            print("Wprowadzono nieodpowiedni znak.")
        pocz, kon = przedzial()
        if metoda == 1:
            if funk == 1:
                bisekcja(fun1, pocz, kon, eps)
            elif funk == 2:
                bisekcja(fun2, pocz, kon, eps)
            elif funk == 3:
                bisekcja(fun3, pocz, kon, eps)
            elif funk == 4:
                bisekcja(fun4, pocz, kon, eps)
            elif funk == 5:
                bisekcja(fun5, pocz, kon, eps)
        elif metoda == 2:
            if funk == 1:
                sieczne(fun1, pocz, kon, eps)
            elif funk == 2:
                sieczne(fun2, pocz, kon, eps)
            elif funk == 3:
                sieczne(fun3, pocz, kon, eps)
            elif funk == 4:
                sieczne(fun4, pocz, kon, eps)
            elif funk == 5:
                sieczne(fun5, pocz, kon, eps)


def main():
    fun_wybor()


main()
