from algorithms import horner
import numpy as np

human_readable_functions = {
    1: "x^5 + 3x^3 - x - 1",
    2: "2x + 3",
    3: "sin(x)",
    4: "exp(1/2x) - 5cos(2(x-1))",
    5: "|-2x + 4 * sin(x)|",
    6: "|x|"
}

functions = {
    1: lambda x: horner([1, 0, 3, 0, -1, -1], x),
    2: lambda x: 2 * x + 3,
    3: lambda x: np.sin(x),
    4: lambda x: np.exp(1 / 2 * x) - 5.0 * np.cos(2 * (x - 1)),
    5: lambda x: np.absolute((-2) * x + 4 * np.sin(x)),
    6: lambda x: np.absolute(x)
}
