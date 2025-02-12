#!/usr/bin/python3
"""module with a function to rotate matrix"""


def rotate_2d_matrix(matrix):
    """rotate 2D matrix"""
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
