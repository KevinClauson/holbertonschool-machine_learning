#!/usr/bin/env python3
"""a function that adds two matrices"""


def add_matrices2D(mat1, mat2):
    """
        A function to add two matrices
        mat1: a matrix
        mat2: a matrix
        Return: a matrix that is sum of other two
    """
    s_matrix = []
    for i, row in enumerate(mat1):
        if len(mat1[i]) != len(mat2[i]):
            return None
        for j, _ in enumerate(mat1[i]):
            if i == 0:
                s_matrix.append([mat1[i][j] + mat2[i][j]])
            else:
                s_matrix[j].append(mat1[i][j] + mat2[i][j])
    return s_matrix
