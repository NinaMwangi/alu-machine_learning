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
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """
        Getter function for W
        :returns weight vector neuron
        """
        return self.__W

    @property
    def b(self):
        """
        Getter function for b
        returns bias for neuron
        """
        return self.__b

    @property
    def A(self):
        """
        Getter function for A
        returns activated output of the neuron
        """
        return self.__A
