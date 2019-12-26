#!/usr/bin/env python3
matrix_shape = __import__('2-size_me_please').matrix_shape

mat1 = [[1, 2], [3, 4]]
print(matrix_shape(mat1))
mat2 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
        [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]]
print(matrix_shape(mat2))

'''
def matrix_shape(matrix):
    """
        Alternate way of solving
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
'''
