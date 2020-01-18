#!/usr/bin/env python3
"""A poison class"""


class Poisson:
    """
        A class
    """
    def __init__(self, data=None, lambtha=1.):
        """
            data: is a list of the data to be used to estimate the distribution
            lambtha: is the expected number of occurences in a given time frame
        """
        if data and lambtha <= 0:
            raise ValueError('lambtha must be a positive value')
        if data and type(data) is not list:
            raise TypeError('data must be a list')
        if data and len(data) < 2:
            raise ValueError('data must contain multiple values')
        if data:
            self.lambtha = (sum(data) / len(data)) / 1.0
        else:
            self.lambtha = lambtha/1.0
