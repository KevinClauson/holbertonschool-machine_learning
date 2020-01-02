#!/usr/bin/env python3
"""calculate polynomials"""


def poly_derivative(poly):
    """
        Calculates the derivative of a polynomial
        poly: is a list of coefficients representing a polynomial
        Return: a new list of coefficients for the derivative of polynomial
    """
    if type(poly) is not list or len(poly) < 1 or type(poly[0]) is not int:
        return None
    der = []
    for i, val in enumerate(poly):
        if i > 0:
            der.append(i * val)
    if len(der) == 0:
        der = [0]
    return der
