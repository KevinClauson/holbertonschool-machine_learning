#!/usr/bin/env python3
"""Calculates the shape of a matrix"""


def matrix_shape(matrix, size=[]):
    """
        Calculates the shape of a matrix using tail recursion
        Seee alternate way in the 2-main file
        matrix: is the array to calculate the shape of
        size: is the shape of the matrix
        Return: size of matrix which is a list of integers
    """
    if type(matrix) is list:
        return matrix_shape(matrix[0], size + [len(matrix)])
    else:
        return size
