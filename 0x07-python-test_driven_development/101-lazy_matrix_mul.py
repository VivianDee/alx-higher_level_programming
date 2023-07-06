#!/usr/bin/python3

import numpy as np

def validate_matrix(matrix, name):
    if not isinstance(matrix, list):
        raise TypeError(f"{name} must be a list")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(f"{name} must be a list of lists")
    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise ValueError(f"{name} can't be empty")
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError(f"each row of {name} must be of the same size")
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError(f"{name} should contain only integers or floats")

def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy.

    Parameters:
    - m_a (numpy.ndarray): The first matrix.
    - m_b (numpy.ndarray): The second matrix.

    Raises:
    - ValueError: If the dimensions of the matrices are incompatible for multiplication.
    """
    validate_matrix(m_a, "m_a")
    validate_matrix(m_b, "m_b")

    if len(m_a) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    if len(m_a[0]) != len(m_b[0]):
        raise ValueError("m_a and m_b can't be multiplied")
    result = np.matmul(m_a, m_b)
    return result
