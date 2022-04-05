import numpy as np
from numpy.linalg import matrix_rank


def switch_rows(M, i, j):
    temp = M[i].copy()
    M[i] = M[j]
    M[j] = temp


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


def check_diagonal(A, b):
    n = len(A)

    for j in range(n):
        max_el, index = A[0][j], 0
        for i in range(1, n):

            if abs(A[i][j]) > abs(max_el):
                max_el, index = A[i][j], i

        switch_rows(A, j, index)
        switch_rows(b, j, index)


def gaussian(A, b):
    n = len(A)
    check_diagonal(A, b)

    for k in range(n - 1):
        for i in range(k + 1, n):

            m = A[i, k] / A[k, k]
            for j in range(k, n):
                A[i, j] -= m * A[k, j]
            b[i] -= m * b[k]

    x = np.zeros(n)
    for k in range(n - 1, -1, -1):  # podstawianie w tyl
        rest = A[k, k + 1:n] @ x[k + 1:n]
        x[k] = (b[k] - rest) / A[k, k]

    return x
