# Metoda eliminacji Gaussa

from choice import file_choice
from functions import gaussian, check

A, b = file_choice()
system_type = check(A, b)

match system_type:
    case "determinate":
        print("Uklad rownan ma dokładnie jedno rozwiązanie:")
        x = gaussian(A, b)

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
