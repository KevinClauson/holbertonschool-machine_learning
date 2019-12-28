#!/usr/bin/env python3
"""Concatenates two matrices along a specific axis"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
        Concats 2 matrices
        mat1: numpy.ndarray
        mat2: numpy.ndarray
        axis: integer that is for the axis
        Return: transpose a matrix on the axis
    """
    return np.concatenate((mat1, mat2), axis=axis)
