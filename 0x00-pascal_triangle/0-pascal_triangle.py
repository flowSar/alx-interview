#!/usr/bin/python3

"""Pascal triangle"""


def pascal_triangle(n):
    """Triangle Pasc"""
    if n <= 0:
        return []
    tri = [[1]]
    for row_number in range(1, n):
        row = [1]
        for j in range(1, row_number):
            element = tri[row_number - 1][j - 1] + tri[row_number - 1][j]
            row.append(element)
        row.append(1)
        tri.append(row)

    return tri
