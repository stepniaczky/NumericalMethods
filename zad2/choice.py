from file_functions import load


def file_choice():
    try:
        choice = input("Nazwa pliku zawierajacego macierz: ")
        return load(choice)
    except FileNotFoundError:
        print("Wprowadzono niepoprawna nazwe pliku\n")
        return file_choice()
