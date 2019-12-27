#!/usr/bin/env python3
"""Transposes a matrix"""


def matrix_transpose(matrix):
    """
        Takes a matrix and returns the transpose
        matrix: a matrix of integers
        Return: a matrix
    """
    t_matrix = []
    for i, row in enumerate(matrix):
        for j, col in enumerate(matrix[i]):
            if i == 0:
                t_matrix.append([matrix[i][j]])
            else:
                t_matrix[j].append(matrix[i][j])
    return t_matrix
