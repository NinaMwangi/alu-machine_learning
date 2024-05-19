#!/usr/bin/env python3


'''
    This script contains a function that performs element-wise addition, subtraction, multiplication, and division.
'''
def np_elementwise(mat1, mat2):
    '''
        The function that will perfome the add, sub, mul and div element wise.
        mat1: First matrix
        mat2: second matrix
        Returns:a tuple containing the element-wise sum, difference, product, and quotient, respectively.
    '''
    addition = mat1 + mat2
    subtraction = mat1 - mat2
    multiplication = mat1 * mat2
    division = mat1 / mat2
    
    return addition, subtraction, multiplication, division
