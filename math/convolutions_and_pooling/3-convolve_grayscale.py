#!/usr/bin/env python3
''' This script runs a function that performs a valid
    convolution on grayscale images.
'''
import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    '''
    The function that convolves the grescale image.
    images: the input images to be convolved.
    kernel: the filter being applied to the images
    m is the number of images
    h is the height in pixels of the images
    w is the width in pixels of the images
    kh is the height of the kernel
    kw is the width of the kernel
    padding: is tuple  of (ph, pw)
    ph is the padding for the height of the image
    pw is the padding for the width of the image
    stride is a tuple of (sh, sw)
    sh is the stride for the height of the image
    sw is the stride for the width of the image
    Returns: a numpy.ndarray containing the convolved images
    '''
    c_images, images_h, images_w = images.shape
    f_height = kernel.shape[0]
    f_width = kernel.shape[1]
    stride_h, stride_w = stride

    if padding == "same":
        padding_h = ((images_h - 1) * stride_h + f_height - images_h) // 2 + 1
        padding_w = ((images_w - 1) * stride_w + f_width - images_w) // 2 + 1
    elif padding == "valid":
        padding_h, padding_w = (0, 0)
    else:
        padding_h, padding_w = padding

    c_height = (images.shape[1] + 2 * padding_h - f_height) // stride_h + 1
    c_width = (images.shape[2] + 2 * padding_w - f_width) // stride_w + 1
    # np.pad works with a before_N and after_N parameter defined in a tuple
    # that will add the selected pad at each dimension
    pad_images = np.pad(images, ((0, 0), (padding_h, padding_h), (padding_w,
                                                                  padding_w)))

    convolved = np.zeros((c_images, c_height, c_width))
    for row in range(c_height):
        for col in range(c_width):
            pad_ele = pad_images[:, row * stride_h:row * stride_h + f_height,
                                 col * stride_w:col * stride_w + f_width]
            sum_mul_ele = np.sum(pad_ele * kernel, axis=(1, 2))
            convolved[:, row, col] = sum_mul_ele
    return convolved
