#!/usr/bin/env python3
"""Calculates the shape of a matrix"""


def matrix_shape(matrix):
    """
        Calculates the shape of a matrix
        matrix: is the array to calculate the shape of

        Return: size of matrix which is a list of integers
    """
    if not matrix or len(matrix) == 0:
        return [0] 

    size = [len(matrix)]
    while type(matrix[0]) is list:
        size.append(len(matrix[0]))
        matrix = matrix[0]
    return size
