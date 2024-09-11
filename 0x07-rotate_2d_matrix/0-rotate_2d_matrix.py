#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
"""


def transpose(matrix):
    """
    swap rows and columns
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_rows(matrix):
    """
    Reverse the rows of a matrix
    """
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    """
    Rotates the matrix 90 degrees clockwise
    """
    transpose(matrix)
    reverse_rows(matrix)
