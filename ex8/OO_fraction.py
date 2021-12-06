class Fraction:
    def __init__(self, num, den):
        """Initializing a Fraction object num / den
        To add check if den is zero
        To add check if num and den are both integers
        >>> f = Fraction(3, 4)
        >>> f.num
        3
        >>> f.den
        4
        >>> print(f)
        3/4
        """

        self.num = num
        self.den = den

    @staticmethod
    def __gcd(a, b):
        """Return the greatest common divisor of a and b

        >>> Fraction._Fraction__gcd(12, 16)
        4

        >>> Fraction._Fraction__gcd(624129, 2061517)
        18913
        """

        if a < 0:
            a = -a
        if b < 0:
            b = -b
        while b != 0:
            t = b
            b = a % b
            a = t
        return a

    def reduce(self):
        """Return a reduced Fraction for this object

        >>> f = Fraction(2, 4)
        >>> print(f.reduce())
        1/2
        """

        g = self.__gcd(self.num, self.den)
        return Fraction(self.num//g, self.den//g)

    def add(self, m):
        """Return the resulting fraction that is the sum of this fraction and the m fraction

        >>> f1 = Fraction(1, 4)
        >>> f2 = Fraction(5, 4)
        >>> print(f1.add(f2))
        3/2
        """

        f_num = self.num*m.den + m.num*self.den
        f_den = self.den*m.den
        f = Fraction(f_num, f_den)
        return f.reduce()

    def __add__(self, m):
        return self.add(m)

    def negate(self):
        """Return the negation of this fraction object
        >>> f = Fraction(6, 8)
        >>> print(f.negate())
        -6/8
        """

        return Fraction(-self.num, self.den)

    def subtract(self, m):
        """Return the resulting fraction that is the difference between this fraction and the m fraction

        >>> f1 = Fraction(1, 4)
        >>> f2 = Fraction(5, 4)
        >>> print(f1.subtract(f2))
        -1/1
        """

        f = m.negate()
        return self.add(f)
    
    def __sub__(self, m):
        return self.subtract(m)
    
    def multiply(self, n):
        """Return the resulting fraction that is the multiplication of this fraction and the m fraction

        >>> f1 = Fraction(1, 4)
        >>> f2 = Fraction(5, 4)
        >>> print(f1.multiply(f2))
        5/16
        """
        
        f_num = self.num*n.num
        f_den = self.den*n.den
        f = Fraction(f_num, f_den)
        return f.reduce()
    
    def __mul__(self, n):
        return self.multiply(n)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)
