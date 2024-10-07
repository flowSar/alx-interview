#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Generate Pascal's Triangle with n rows."""
    if n <= 0:
        return []

    triangle = [[1]]

    for row_number in range(1, n):
        row = [1]
        for j in range(1, row_number):
            element = triangle[row_number - 1][j - 1]
            element += triangle[row_number - 1][j]
            row.append(element)
        row.append(1)
        triangle.append(row)

    return triangle
