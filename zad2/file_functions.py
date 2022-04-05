import numpy as np


def load(filename):
    try:
        Ab = np.loadtxt(f'equations/{filename}.txt')

        n = len(Ab[0]) - 1  # index ostatniej kolumny
        A, b = Ab[:, :n], Ab[:, n]
        return A, b
    except ValueError:
        exit("Macierz w pliku jest niepoprawna!")
