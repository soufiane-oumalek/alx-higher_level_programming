#!/usr/bin/python3
"""Matrix_devided method"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix

    Returns a new matrix"""
    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    i = 0
    while i < len(matrix):
        row = matrix[i]
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")

        j = 0
        while j < len(row):
            n = row[j]
            if type(n) is not int and type(n) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
            j += 1
        i += 1

    l_row = []
    for row in matrix:
        l_row.append(len(row))
    if not all(elm == l_row[0]for elm in l_row):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(dive) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    n_mtrx = [[round(n / div, 2) for x in row]for row in matrix]
    return n_mtrx
