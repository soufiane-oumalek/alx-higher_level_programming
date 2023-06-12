#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j, c  in enumerate(i):
            if j != len(i) - 1:
                print("{:d}".format(c), end="")
            else:
                print("{:d}".format(c), end=" ")
        print()
