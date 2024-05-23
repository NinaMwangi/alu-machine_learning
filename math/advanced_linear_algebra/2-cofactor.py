#!/usr/bin/env python3
'''
    This script calculates the determinant of a matrix.
'''

def determinant(matrix):
    '''
        The function that will calculate the determinant.
    '''
    if type(matrix) is not list:
        raise TypeError("matrix must be a list of lists")

    if matrix == [[]]:
        return 1

    for i in range(len(matrix)):
        if len(matrix) != len(matrix[i]):
            raise ValueError("matrix must be a square matrix")
        if type(matrix[i]) is not list or not len(matrix[i]):
            raise TypeError("matrix must be a list of lists")

    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]

    if len(matrix) == 2 and len(matrix[0]) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    # Recursive: calculating the det using cofactor expansion
    det = 0
    for j in range(len(matrix[0])):
        if matrix[0]:
            cofactor = matrix[0][j] * determinant([row[:j] + row[j+1:] \
                for row in matrix[1:]])
            det += cofactor * (-1) ** j
    return det

def cofactor(matrix):
    '''
    a function that calculates the minor of a matrix
    '''
    if type(matrix) is not list or not len(matrix):
        raise TypeError("matrix must be a list of lists")

    if matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")

    for i in range(len(matrix)):
        if len(matrix) != len(matrix[i]):
            raise ValueError("matrix must be a non-empty square matrix")
        if type(matrix[i]) is not list or not len(matrix[i]):
            raise TypeError("matrix must be a list of lists")

    if len(matrix) == 1:
        return [[1]]

    list_minor = []
    for i in range(len(matrix)):
        inner = []
        if i % 2 == 0:
            cof = 1
        else:
            cof = -1
        for j in range(len(matrix[0])):
            next_matrix = [x[:] for x in matrix]
            del next_matrix[i]
            for mat in next_matrix:
                del mat[j]
            det = determinant(next_matrix) * cof
            inner.append(det)
            cof = cof * -1
        list_minor.append(inner)

    return list_minor
