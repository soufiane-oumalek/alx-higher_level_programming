#!/usr/bin/python3
"""triangle function"""


def pascal_triangle(n):
    """Create a function that returns a list of lists
    of integers representing the Pascal's triangle of n
    """
    if n < 0:
        return []
    triangle = [[1]]
    x = 1

    while x < n:
        r = [1]
        y = 1
        while y < x:
            r.append(triangle[x-1][y-1] + triangle[x-1][y])
            y += 1
        r.append(1)
        triangle.append(r)
        x += 1
    return triangle
