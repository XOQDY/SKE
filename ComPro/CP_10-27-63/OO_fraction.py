from math import gcd
class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def reduce(self):
        """Returns a reduced form of this fraction
        """
        d = gcd(self.num, self.den)
        self.num /= d
        self.den /= d

    def add(self, m):
        """Returns a new fraction in reduced form that results from adding this fraction with the m fraction
        """
        self.num += self.den * m

    def subtract(self, m):
        """Returns a new fraction in reduced form that results from subtracting this fraction with the m fraction
        """
        self.num -= self.den * m
    
    def multiply(self, n):
        """Returns a new fraction in reduced form that results from multiplying this fraction with the n fraction
        """
        self.num *= n
        self.den *= n
