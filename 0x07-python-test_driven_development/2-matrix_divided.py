#!/usr/bin/python3
""" function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix
    Args:
        matrix: list for int or float
        div: the divition
        """
    if not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):