#!/usr/bin/pyhton3
def square_matrix_simple(matrix=[]):
    return [list(map(lambda x: x ** 2, rw)) for rw in matrix]
