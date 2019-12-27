#!/usr/bin/env python3
"""multiplication of 2 matrices"""


def mat_mul(mat1, mat2):
    """
        multiplication of 2 matrices
        mat1: matrix
        mat2: matrix
        Return: a new matrix or none if can't be multiplied
    """
    if len(mat1[0]) != len(mat2):
        return None
    m_mat = []
    for i in range(len(mat1)):
        m_mat.append([])
        for j in range(len(mat1[i])):
            for y in range(len(mat2[0])):
                if j == 0:
                    m_mat[i].append(mat1[i][j] * mat2[0][y])
                else:
                    m_mat[i][y] += (mat1[i][j] * mat2[j][y])
    return m_mat
