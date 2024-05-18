#!/usr/bin/env python3
'''
The script contains a function that adds two arrays element wise.
'''
def add_arrays(arr1, arr2):
    '''
        The function that adds two arrays element wise.
        arr1: The first array
        arr2: The second array
        Returns: A list containing sums of arr1 & arr2. If not same shape returns none.
    '''
    if len(arr1) != len(arr2):
        return None

    # Element wise addition using list comprehension
    return [a + b for a, b in zip(arr1, arr2)]

# Testcase
add_arrays = __import__('4-line_up').add_arrays

arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
print(add_arrays(arr1, arr2))
print(arr1)
print(arr2)
print(add_arrays(arr1, [1, 2, 3]))
