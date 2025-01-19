#!/usr/bin/env python3
"""
Module to create a Neuron
"""
import numpy as np


class Neuron:
    """
    Class that defines a single neuron
    """

    def __init__(self, nx):
        """
        class constructor
        :param nx is the number of input features for this neuron
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.nx = nx
        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0
