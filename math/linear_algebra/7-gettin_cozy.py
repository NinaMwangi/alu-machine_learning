#!/usr/bin/env python3

'''
    This scriptnconcatenates 2 matrices along a specific axis.
'''


def cat_matrices2D(mat1, mat2, axis=0):
    '''
        The function that concatenates 2 matrices along a specific axis.
        mat1: matrix one
        mat2: matrix two
        axis: The axis along which to concatenate, the default is 0.
        returns a new matrix or None if the matrices dont have the same shapa.
    '''
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    else:
        return None
