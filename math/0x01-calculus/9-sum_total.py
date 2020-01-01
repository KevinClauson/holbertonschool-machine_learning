#!/usr/bin/env python3
"""Function that returns sum of squares"""


def summation_i_squared(n):
    """
        Function that takes an integer and returns the square of all ints
        from 1 to that integer and including that integer.
        n: integer
        Return: an integer of the sum
    """
    if not isinstance(n, int) or n <= 0:
        return None
    return int((2*(n**3)+(3*(n**2))+n)/6)
