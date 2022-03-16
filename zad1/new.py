functions = ["f(x) = x^3 - x^2 - 2x + 1",
             "f(x) = 2^x - 3x",
             "f(x) = x^3 - x + 1",
             "f(x) = 2 + cos(2x)",
             "f(x) = sin(x) - cos(x)"]


def fun():
    print("---FUNKCJE---")
    for i, fn in enumerate(functions):
        print(str(i + 1) + ":", fn)


def main():
    fn = int
    # Wybor funkcji
    while fn not in [1, 2, 3, 4, 5]:
        fun()
        try:
            fn = int(input("Twoj wybor: ")) - 1
        except ValueError:
            print("Wprowadzono zla wartosc!\n")

    # Wybor przedzialu
    print("\n---PRZEDZIAL")
    x1, x2 = "err", "err"
    while x1 or x2 != float:
        try:
            x1 = float(input("Podaj przedzial poczatkowy: "))
            x2 = float(input("Podaj przedzial koncowy: "))
        except ValueError:
            print("Blad!")
    print(x1, x2)


main()
