#!/usr/bin/env python3
""" concatenates two matrices along a specific axis """


def cat_matrices2D(mat1, mat2, axis=0):
    """
        Concats 2 matrices
        mat1: 2D matrix
        mat2: 2D matrix
        axis: if default 0 then concat row-wise, if 1 then col-wise
        Return: None if can't concat otheriwse the new matrix
    """
    if axis < 0 or axis > 1:
        return None
    if axis == 1 and len(mat1) != len(mat2):
        return None
    if axis == 0 and len(mat1[0]) != len(mat2[0]):
        return None
    c_mat = []
    for i in range(len(mat1)):
        c_mat.append([])
        for j in range(len(mat1[i])):
            c_mat[i].append(mat1[i][j])
    if axis == 0:
        for j in range(len(mat2)):
            c_mat.append(mat2[j])
    if axis == 1:
        for j in range(len(mat1)):
            for i in range(len(mat2[j])):
                c_mat[j].append(mat2[j][i])
    return c_mat
