#!/usr/bin/env python3
"""that calculates the integral of a polynomial"""


def poly_integral(poly, C=0):
    """
        A function that calculated the integral of a polynomial
        poly: is a list of coefficients representing a polynomial
        C: is an integer representing the integration constant
        Return: a new list of coefficients representing the integral
        of the polynomial
    """
    integral = [C]
    for i, val in enumerate(poly):
        if val % (i+1):
            integral.append(val/(i+1))
        else:
            integral.append(val//(i + 1))
    return integral
