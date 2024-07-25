#!/usr/bin/python3
"""
A function def pascal_triangle(n)
"""

from math import factorial


def pascal_triangle(n):
    """returns a list of lists of integers representing the
    Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            coefficient = factorial(i) / (factorial(j) * factorial(i - j))
            row.append(int(coefficient))
        triangle.append(row)
    return triangle
