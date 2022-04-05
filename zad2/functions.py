import numpy as np
from numpy.linalg import matrix_rank


def switch_rows(A, i, j):
    n = A.shape[0]
    E = np.eye(n)
    E[i, i] = 0
    E[j, j] = 0
    E[i, j] = 1
    E[j, i] = 1
    return E @ A


def scale_row(A, k, i):
    n = A.shape[0]
    E = np.eye(n)
    E[i, i] = k
    return E @ A


def add_row(A, k, i, j):
    n = A.shape[0]
    E = np.eye(n)
    if i == j:
        E[i, i] = k + 1
    else:
        E[i, j] = k
    return E @ A


def check(A, b):
    U = np.c_[A, b]
    rankA = matrix_rank(A)
    rankU = matrix_rank(U)

    if rankA != rankU:
        return "contradictory"
    else:
        if rankA == len(A[0]):
            return "determinate"
        elif rankA < len(A[0]):
            return "indeterminate"


def diagonally_dominant(A, b):
    n = len(A)

    flag = True
    for j in range(n):
        max_, row = A[0][j], 0
        for i in range(1, n):
            if abs(A[i][j]) > abs(max_):
                max_, row = A[i][j], i
        A = switch_rows(A, j, row)
        b = switch_rows(b, j, row)

    for j in range(n):
        max_ = A[j][j]
        for i in range(j + 1, n):
            if abs(max_) == abs(A[i][j]):
                flag = False  # macierz nie jest przekatniowo dominujaca

    return A, b, flag


def gaussian(A, b):
    n = len(A)
    flag = True

    A, b, flag = diagonally_dominant(A, b)

    n = len(b)
    for k in range(n - 1):  # rows
        for i in range(k + 1, n):  # columns

            s = A[i, k] / A[k, k]
            for j in range(k, n):
                A[i, j] -= s * A[k, j]
            b[i] -= s * b[k]

    for k in range(n - 1, -1, -1):  # rows
        b[k] = (b[k] - np.dot(A[k, k + 1:n], b[k + 1:n])) / A[k, k]

    return b, flag
