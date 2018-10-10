"""
This file contains definition of a fraction class.

You should put complete class here. It must be named `Fragion` and must have the following properties:

- four basic mathematical operators defined;
- elegant conversion to string in the form '3/2';
- simplification and clean-up on construction: both attribute divided by the greatest common divisor
  sign in the nominator, denominator not zero (ValueError should be raised in such case), both attributes
  must be integers (ValueError if not),
- method `value` returning float value of the fraction.
"""
from math import gcd


class Fraction(object):
    """
    Fraction class.
    """

    def __init__(self, nom, denom):
        self.nom = nom/gcd(nom, denom)
        self.denom = denom/gcd(nom, denom)

        if self.denom == 0:
            raise ValueError('denominator cannot be 0.')

        if self.denom < 0:
            self.nom = - self.nom
            self.denom = - self.denom

        self.nom = int(self.nom)
        self.denom = int(self.denom)

    def __str__(self):
        return ('{0.nom}/{0.denom}'.format(self))

    def __mul__(self, other):
        return Fraction(self.nom * other.nom, self.denom * other.denom)

    def __truediv__(self, other):
        return Fraction(self.nom * other.denom, self.denom * other.nom)

    def __add__(self, other):
        return Fraction(self.nom*other.denom + other.nom*self.denom, self.denom *other.denom)

    def __sub__(self, other):
        return Fraction(self.nom * other.denom - other.nom * self.denom, self.denom * other.denom)

    def __pow__(self, power, modulo=None):
        return Fraction(self.nom**power, self.denom**power)

    def __repr__(self):
        return f"Fraction({self.nom}, {self.denom})"

    def __eq__(self, other):
        return self.nom == other.nom and self.denom == other.denom

    def value(self):
        return  self.nom/self.denom