#!/usr/bin/env python3
''' This script runs a function that performs a same
    convolution on grayscale images.
'''
import numpy as np


def convolve_grayscale_same(images, kernel):
    '''
    The function that convolves the grescale image.
    images: the input images to be convolved.
    kernel: the filter being applied to the images
    m is the number of images
    h is the height in pixels of the images
    w is the width in pixels of the images
    kh is the height of the kernel
    kw is the width of the kernel
    return: numpy.ndarray containing the convolved images
    '''
    c_images = images.shape[0]
    f_height = kernel.shape[0]
    f_width = kernel.shape[1]

    # calculating padding if filter dimensions are odd or even
    if f_height % 2 != 0:
        padding_h = (f_height - 1) // 2
    else:
        padding_h = f_height // 2

    if f_width % 2 != 0:
        padding_w = (f_width - 1) // 2
    else:
        padding_w = f_width // 2

    c_height = images.shape[1]
    c_width = images.shape[2]

    pad_images = np.pad(images, ((0, 0), (padding_h, padding_h), (padding_w,
                                                                  padding_w)))
    convolved = np.zeros((c_images, c_height, c_width))
    for row in range(c_height):
        for col in range(c_width):
            ele_mul = pad_images[:, row:row + f_height, col:col + f_width] * \
                kernel
            ele_sum = np.sum(ele_mul, axis=(1, 2))
            convolved[:, row, col] = ele_sum

    return convolved
