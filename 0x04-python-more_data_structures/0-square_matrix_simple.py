#!/usr/bin/pyhton3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        res = list(map(lambda x: x ** 2, row))
        new_matrix.append(res)
    return new_matrix
