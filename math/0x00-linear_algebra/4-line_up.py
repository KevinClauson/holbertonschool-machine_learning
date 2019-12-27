#!/usr/bin/env python3
"""adding matrix"""


def add_arrays(arr1, arr2):
    """
        Adding 2 matrix
        arr1: is one matrix
        arr2: is the other matrix
        Return: the result or none if
        the matrix are not the same size
    """
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]
