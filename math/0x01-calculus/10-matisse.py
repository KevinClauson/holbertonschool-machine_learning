#!/usr/bin/env python3
"""calculate polynomials"""


def poly_derivative(poly):
    """
        Calculates the derivative of a polynomial
        poly: is a list of coefficients representing a polynomial
        Return: a new list of coefficients for the derivative of polynomial
    """
    if not poly:
        return None
    der = []
    for i, val in enumerate(poly):
        if i > 0:
            der.append(i * val)
    return der
