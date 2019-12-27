#!/usr/bin/env python3
"""a function that adds two matrices"""


def add_matrices2D(mat1, mat2):
    """
        A function to add two matrices
        mat1: a matrix
        mat2: a matrix
        Return: a matrix that is sum of other two
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    s_matrix = []
    for i in range(len(mat1)):
        s_matrix.append([])
        for j in range(len(mat1[0])):
            s_matrix[i].append(mat1[i][j]+mat2[i][j])
    return s_matrix
