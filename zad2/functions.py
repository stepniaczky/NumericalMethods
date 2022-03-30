import numpy as np
from numpy.linalg import matrix_rank


# def switch_rows(A, i, j):
#     n = A.shape[0]
#     E = np.eye(n)
#     E[i, i] = 0
#     E[j, j] = 0
#     E[i, j] = 1
#     E[j, i] = 1
#     return E @ A
#
#
# def scale_row(A, k, i):
#     n = A.shape[0]
#     E = np.eye(n)
#     E[i, i] = k
#     return E @ A
#
#
# def add_row(A, k, i, j):
#     n = A.shape[0]
#     E = np.eye(n)
#     if i == j:
#         E[i, i] = k + 1
#     else:
#         E[i, j] = k
#     return E @ A


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


def gaussian(A, b):
    n = len(b)  # number of rows

    for k in range(0, n - 1):  # rows
        for i in range(k + 1, n):  # columns
            if A[i, k] != 0.0:
                factor = A[i, k] / A[k, k]
                A[i, k + 1:n] = A[i, k + 1:n] - np.multiply(factor, A[k, k + 1:n])
                b[i] -= np.multiply(factor, b[k])

    for k in range(n - 1, -1, -1):  # rows
        b[k] = (b[k] - np.dot(A[k, k + 1:n], b[k + 1:n])) / A[k, k]

    return b
