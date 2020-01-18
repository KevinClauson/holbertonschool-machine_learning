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
        if not data:
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
            else:
                self.lambtha = lambtha/1.0
        if data:
            if type(data) is not list:
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.lambtha = (sum(data) / len(data)) / 1.0
