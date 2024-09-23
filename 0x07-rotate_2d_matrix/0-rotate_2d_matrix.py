#!/usr/bin/python3
"""
Rotate 2d matrix
"""
from typing import List


def rotate_2d_matrix(matrix: List[List]):
    """
    rotate 2d matrix
    """
    matrix.reverse()
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(i, len(matrix)):
            element = matrix[j][i]
            matrix[j][i] = matrix[i][j]
            matrix[i][j] = element
