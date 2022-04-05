# Metoda eliminacji Gaussa

from choice import file_choice
from functions import gaussian, check
import time


if __name__ == '__main__':
    A, b = file_choice()
    system_type = check(A, b)

    match system_type:
        case "determinate":
            start = time.time_ns()
            x, flag = gaussian(A, b)
            total = (time.time_ns() - start) / 1000000
            print(f"Czas pracy algorytmu eliminacji Gaussa: {total}ms\n")

            if flag is True:
                print(f"Macierz jest przekatniowo dominujaca!")
            else:
                print(f"Macierz nie jest przekatniowo dominujaca!")
                print(f"(Uzyskane wyniki mogą byc bledne")

            print("Uklad rownan ma dokładnie jedno rozwiązanie:")

            result = ""
            for i in range(len(x)):
                if i != 0:
                    result += ", "
                result += f"x{i + 1} = {x[i]}"

            print(result)

        case "indeterminate":
            print("Uklad rownan jest nieoznaczony")
        case "contradictory":
            print("Uklad rownan jest sprzeczny!")
