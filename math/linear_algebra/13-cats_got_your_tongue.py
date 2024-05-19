#!/usr/bin/env python3
'''
    This script contains a function that concatenates 2 matrices in a specific axis
'''


import numpy as np


def np_cat(mat1, mat2, axis=0):
    '''
        function that Concatenate two arrays based on an axis
    '''
    return np.concatenate((mat1, mat2), axis=axis)
