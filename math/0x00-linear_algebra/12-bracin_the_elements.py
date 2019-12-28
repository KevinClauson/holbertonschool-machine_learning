#!/usr/bin/env python3
"""performs add, sub, mult, and div"""

import numpy as np


def np_elementwise(mat1, mat2):
    """
        A mult, add, sub, div of matrices
        mat1: a numpy array
        mat2: a numpy array
        Return: tuple containing the
        element-wise sum, difference, product,
        and quotient, respectively        
    """
    return (np.add(mat1, mat2), np.subtract(mat1, mat2),
           np.multiply(mat1, mat2), np.divide(mat1, mat2))
