#!/usr/bin/pyhton3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for rw in matrix:
        square_matrix = list(map(lambda x: x**2, rw))
        new_matrix.append(square_matrix)
    return new_matrix
