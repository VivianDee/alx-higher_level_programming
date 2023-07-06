#!/usr/bin/python3

"""
    Function matrix_mul
"""

def validate_matrix(matrix, name):
    """validates the matrix"""
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

def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Parameters:
    - m_a (list of lists): The first matrix.
    - m_b (list of lists): The second matrix.

    Raises:
    - TypeError: If `m_a` or `m_b` is not a list, or if the elements of `m_a` or `m_b` are not integers or floats,
        or if `m_a` or `m_b` is not a rectangle (rows of different sizes).
    - ValueError: If `m_a` or `m_b` is empty (i.e., `[]` or `[[]]`), or if `m_a` and `m_b` cannot be multiplied.
    """
    validate_matrix(m_a, "m_a")
    validate_matrix(m_b, "m_b")
    if len(m_a[0]) != len(m_b[0]):
        raise ValueError("m_a and m_b can't be multiplied")
    if len(m_a[0]) != len(m_b[0]):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_a[0])))
            row.append(element)
        result.append(row)

    return result
