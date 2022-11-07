#!/usr/bin/python3
"""function that divides elements"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    matrix2 = []
    length = len(matrix[0])
    for i in range(len(matrix)):
        if length != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        matrix2.append([])
        for j in matrix[i]:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("matrix must be a matrix
                                (list of lists) of integers/float")
            matrix2[i].append(round(j / div, 2))
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif type(div) == 0:
        raise ZeroDivisionError("division by zero")
    return matrix2
