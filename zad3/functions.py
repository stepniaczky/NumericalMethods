from algorithms import horner
import numpy as np

human_readable_functions = {
    1: "|x|",
    2: "x^5 + 3x^3 - x - 1",
    3: "7cos(x-1) - 2sin(x)",
    4: " 6^x - 2x - 5",
    5: "2cos(x) - 1^x - x^3",
    6: "exp(1/2x) - 5cos(2(x-1))",
    7: "|2 * cos(2x) + 2|"
}

functions = {
    1: lambda x: np.absolute(x),
    2: lambda x: horner([1, 0, 3, 0, -1, -1], x),
    3: lambda x: 7.0 * np.cos(x-1) - 2.0 * np.sin(x),
    4: lambda x: 6**x - 2 * x - 5,
    5: lambda x: 2.0 * np.cos(x) - 1.0**x - x**3.0,
    6: lambda x: np.exp(1/2*x) - 5.0 * np.cos(2*(x-1)),
    7: lambda x: np.absolute(2*np.cos(2*x)+2)
}
