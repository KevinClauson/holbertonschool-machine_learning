#!/usr/bin/env python3
"""a function to concat 2 arrays"""


def cat_arrays(arr1, arr2):
    """
        function concats two lists
        arr1: list of ints
        arr2: list of ints
        Return: a list of ints
    """
    return [x for x in arr1+arr2]
