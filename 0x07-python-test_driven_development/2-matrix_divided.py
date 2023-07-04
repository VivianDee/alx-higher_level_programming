#!/usr/bin/python3
"""
    A matrix_divided function
"""


def matrix_divided(matrix, div):
    """
        The matrix_divided function divides all elements of a matrix

        Args:
            matrix (list): A matrix of integers or floats.
            div (int or float): The number to divide the matrix elements by.

        Raises:
            TypeError: If matrix is not a matrix of integers/floats.
            TypeError: If element of the matrix is not an integer or float.
            TypeError: If each row of the matrix does not have the same size.
            TypeError: If the div parameter is not a number (integer or float).
            ZeroDivisionError: If the div parameter is zero (division by zero).

        Returns: A new matrix with the divided results
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                     for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
