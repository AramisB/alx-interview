Rotating a 2D Matrix in Python
This guide provides an overview of how to rotate a 2D matrix by 90 degrees clockwise using Python. It covers matrix representation, in-place operations, matrix transposition, and reversing rows, including different methods for matrix transposition using both standard Python and the NumPy library.

Matrix Representation
In Python, a 2D matrix is represented using a list of lists. Each inner list represents a row in the matrix.

Example:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Rotating a 2D Matrix
To rotate a matrix by 90 degrees clockwise:
Transpose the matrix: Swap rows and columns.
Reverse each row: This achieves the 90-degree clockwise rotation.

Here is a Python implementation that rotates a 2D matrix by 90 degrees clockwise:

def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def reverse_rows(matrix):
    for row in matrix:
        row.reverse()

def rotate_matrix(matrix):
    transpose(matrix)
    reverse_rows(matrix)

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_matrix(matrix)
print(matrix)
# Output:
# [
#   [7, 4, 1],
#   [8, 5, 2],
#   [9, 6, 3]
# ]

Different Methods to Transpose a Matrix
There are multiple ways to transpose a matrix in Python:

1. Using Loops (In-Place)
You can transpose a matrix using nested loops to swap elements:
def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

2. Using numpy.transpose
The NumPy library provides a convenient function, numpy.transpose, to transpose a matrix.

import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

transposed_matrix = np.transpose(matrix)
print(transposed_matrix)
# Output:
# [
#   [1, 4, 7],
#   [2, 5, 8],
#   [3, 6, 9]
# ]
3. Using NumPy .T Attribute
You can also use the .T attribute to transpose a matrix in NumPy.
import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

transposed_matrix = matrix.T
print(transposed_matrix)
# Output:
# [
#   [1, 4, 7],
#   [2, 5, 8],
#   [3, 6, 9]
# ]
In-Place Operations
In-place operations are important for minimizing space complexity by modifying the original matrix directly rather than creating a copy. This is particularly useful for large datasets or matrices where memory usage is a concern.

Conclusion
Rotating a 2D matrix by 90 degrees clockwise involves transposing the matrix and then reversing its rows. There are various ways to perform matrix transposition in Python, including using nested loops or leveraging NumPy's efficient functions.

Requirements
To use the NumPy methods for transposing a matrix, you must have NumPy installed. You can install it using:
pip install numpy