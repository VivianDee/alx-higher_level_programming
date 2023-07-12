#!/usr/bin/python3

"""The pascal_triangle function"""


def pascal_triangle(n):
    """Returns the Pascal’s triangle of n"""
    if n <= 0:
        return []
    triangle = [[1]]

    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            element = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(element)

        row.append(1)
        triangle.append(row)

    return triangle
