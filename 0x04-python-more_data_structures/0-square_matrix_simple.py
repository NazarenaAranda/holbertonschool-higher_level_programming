#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nueva = matrix.copy()
    for n in range(len(matrix)):
        nueva[n] = (list(map(lambda x: x * x, nueva[n])))
        return nueva
