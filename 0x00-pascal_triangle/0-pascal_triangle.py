#!/usr/bin/python3
"""
A function def pascal_triangle(n)
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the
    Pascal’s triangle of n
    """
    triangle = []

    if n <= 0:
        return triangle

    triangle = [[1]]
    while len(triangle) != n:
        row = [1]
        for i in range(len(triangle[-1]) - 1):
            row.append(triangle[-1][i] + triangle[-1][i + 1])
        row.append(1)
        triangle.append(row)
    return triangle
