#!/usr/bin/env python3
'''
   This scrpt contains a function that multiplies 2 matrices.
'''
def mat_mul(mat1, mat2):
    '''
        Multiplies 2 matrices.
        mat1: matrix 1
        mat2: matrix 2
        Returns: A new  matrix and None if the 2 matrices cant be multiplied.
    '''
    if len(mat1[0]) == len(mat2):
        return [
            [
                sum([mat1[i][k] * mat2[k][j] for k in range(len(mat1[0]))])
                for j in range(len(mat2[0]))
            ]
            for i in range(len(mat1))
        ]
    else:
        return None
