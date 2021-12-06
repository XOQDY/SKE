from OO_complex import *
import copy
import numpy as np


class Polynomial:

    def __init__(self, coefficients):
        """initializes the coeffs attribute to be a list of floating-point coefficient values.
        >>> coeffs = Polynomial([1, 2, 3])
        >>> type(coeffs.coefficients)
        <class 'list'>
        """
        self.coefficients = coefficients

    def add(self, other):
        """returns a new Polynomial representing the sum ofPolynomials self and other. Be sure that performing any
        operation on polynomials
        >>> p = Polynomial([1, 2, 3])
        >>> p2 = Polynomial([100, 200])
        >>> print(p.add(p2))
        1(z**2) + 102(z) + 203
        """
        x = copy.deepcopy(Polynomial(self.coefficients))
        for i in range(-1, (len(other.coefficients) * -1) - 1, -1):
            x.coefficients[i] += other.coefficients[i]
        return x

    def val(self, v):
        """returns the numerical result of evaluating the polynomial when x equals v.
        >>> p = Polynomial([1, 2, 3])
        >>> print(p(1))
        6
        """
        d = []
        for x in range(len(self.coefficients)):
            d.append(self.coefficients[x] * (v ** (len(self.coefficients) - (x + 1))))
        return sum(d)
    
    def mul(self, other):
        """returns a new Polynomial representing the product of Polynomials self and other
        >>> p = Polynomial([1, 2, 3])
        >>> print(p.mul(p))
        1(z**4) + 4(z**3) + 10(z**2) + 12(z) + 9
        """
        exponential = {}
        exponential_2 = {}
        result = {}
        for i in range(len(self.coefficients)):
            exponential[len(self.coefficients) - (i + 1)] = self.coefficients[i]
        for i in range(len(other.coefficients)):
            exponential_2[len(self.coefficients) - (i + 1)] = other.coefficients[i]
        for y in exponential:
            for z in exponential_2:
                result[y + z] = 0
        for y in exponential:
            for z in exponential_2:
                result[y + z] += exponential[y] * exponential_2[z]
        result_list = []
        for z in result:
            result_list.append(result[z])
        x = Polynomial(result_list)
        return x
    
    def coeff(self, i):
        """returns the coefficient of the xi term of the polynomial.
        >>> p = Polynomial([1, 2, 3])
        >>> p.coeff(5)
        1
        """
        return self.coefficients[(len(self.coefficients) - 1) - i]
    
    def roots(self):
        if len(self.coefficients) > 2:
            return 'Order too high to solve for roots.'
        else:
            return np.roots([self.coefficients])

    def __call__(self, v):
        return self.val(v)

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.mul(other)

    def __str__(self):
        d = ''
        for x in range(len(self.coefficients)):
            if self.coefficients[x] == 0:
                pass
            elif len(self.coefficients) - (x + 1) > 1:
                d += f'{self.coefficients[x]}(z**{len(self.coefficients) - (x + 1)}) + '
            elif len(self.coefficients) - (x + 1) == 1:
                d += f'{self.coefficients[x]}(z) + '
            else:
                d += f'{self.coefficients[x]}'
        return d


if __name__ == '__main__':
    import doctest

    doctest.testmod()
