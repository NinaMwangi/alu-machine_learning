#!/usr/bin/env python3
'''
    This scripts calculates the shape of a matrix.
'''


def matrix_shape(matrix):
    '''
        This function calculates the shape of a matrix.
        Matrix: A list representing the matrix.
        Returns a list of integers that represents the shape of the matrix.
    '''
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
