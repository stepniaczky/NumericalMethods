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
